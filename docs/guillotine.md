### Guillotine 算法

  ![Guillotine 渲染](https://raw.githubusercontent.com/ssbothwell/greedypacker/master/static/guillotineAlgorithm-best_shortsideHeuristic.png)

  将物品放入箱子，从其左下角开始。对于每次插入，将箱子分割成更小的部分（FreeRectangles），并将它们记录在一个列表中。每当插入新物品时，找到一个 FreeRectangle，使用任何启发式方法，然后将物品放入该 FreeRectangle 的左下角。如果 FreeRectangle 中有剩余的宽度或高度，那么将 FreeRectangle 拆分，以便剩余的空间形成自己的 FreeRectangle（或多个）。

  示例代码：
  ```
  M = greedypacker.BinManager(8, 4, pack_algo='guillotine', heuristic='best_longside', rectangle_merge=True, rotation=True)
  ```

#### 启发式选择
* best_shortside:
  选择一个 FreeRectangle（F），其中插入物品（I）后较短的剩余边最小化。即，选择最小的 min(Fw - Iw, Fh - Ih)。如果平局，则使用 `best_long` 来决定。
* best_longside:
  选择一个 FreeRectangle（F），其中插入物品（I）后较长的剩余边最小化。即，选择最小的 max(Fw - Iw, Fh - Ih)。如果平局，则使用 `best_shortside` 来决定。
* best_area:
  选择一个能容纳物品的最小面积的 FreeRectangle。如果平局，则使用 `best_shortside` 来决定。
* worst_shortside:
  选择一个 FreeRectangle（F），其中插入物品（I）后较短的剩余边最小化。即，选择最大的 min(Fw - Iw, Fh - Ih)。如果平局，则使用 `worst_long_side` 来决定。
* worst_longside:
  选择一个 FreeRectangle（F），其中插入物品（I）后较长的剩余边最小化。即，选择最大的 max(Fw - Iw, Fh - Ih)。如果平局，则使用 `worst_shortside` 来决定。
* worst_area:
  选择一个能容纳物品的最大面积的 FreeRectangle。如果平局，则使用 `worst_shortside` 来决定。

#### 可选优化：

所有优化都是在创建 GreedyPacker 实例时作为关键字参数传入的：

###### 矩形合并
Guillotine 算法倾向于在 FreeRectangles 中留下碎片化的分组，这些碎片可以潜在地连接成更大的 FreeRectangles。这个优化在每次插入物品之间对 FreeRectangle 列表进行碎片整理。

使用方法：
```
M = greedypacker.BinManager(8, 4, 'guillotine', 'best_width_fit', rectangle_merge=True)
```

###### 拆分规则
在 Guillotine 切割中，我们可以选择沿水平轴或垂直轴进行拆分。默认情况下，Greedypacker 将沿水平轴进行拆分。但是，Jukka 指定了 6 种不同的拆分规则，可以产生比默认始终水平拆分更有效的装箱结果。

* 'SplitShorterLeftoverAxis' - 如果剩余的 FreeRectnage 宽度（freerectangle.width - item.width）小于剩余的高度，则在水平轴上进行拆分。
* 'SplitLongerLeftoverAxis' - 如果剩余的 FreeRectnage 宽度（freerectangle.width - item.width）大于剩余的高度，则在水平轴上进行拆分。
* 'SplitShorterAxis' - 如果 FreeRectangle.width <= FreeRectangle.height，则在水平轴上拆分。否则，在垂直轴上拆分。
* 'SplitLongerAxis' - 如果 FreeRectangle.width >= FreeRectangle.height，则在水平轴上拆分。否则，在垂直轴上拆分。
* 'SplitMinimizeArea' - 计算物品上方（A0）和右侧（A1）的象限面积。拆分矩形，以使物品上方和右侧的空间（A3）与较小的象限连接起来。
* 'SplitMaximizeArea' - 与 SplitMinimizeArea 相同，但 A3 与较大的象限连接。

使用方法：
```
M = greedypacker.BinManager(8, 4, 'guillotine', 'best_width_fit', split_heuristic='SplitMinimizeArea')
```
