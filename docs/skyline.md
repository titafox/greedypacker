### Skyline 算法

  ![Skyline 渲染](https://raw.githubusercontent.com/ssbothwell/greedypacker/master/static/skylineAlgorithm-bottom_leftHeuristic.png)

  与跟踪所有 FreeRectangles 或货架的列表不同，Skyline 算法从底部到顶部填充列表，只跟踪填充到箱子中的最顶部物品的顶边。这创建了一个'天际线'或包络。天际线列表随着填充的物品数量线性增长。

由于它只跟踪最顶部的边缘，这个算法是有损的，有可能丧失跟踪到被天际线困住的可用空间的潜力。这可以通过使用 Shelf 算法的 wastemap 优化来抵消。

```
S = greedypacker.BinManager(8, 4, pack_algo='skyline', heuristic='bottom_left', rotation=True)
```

#### 启发式方法
* bottom_left:
  请参阅上面的 Maximal Rectangle bottom_left。
* best_fit:
  将物品放在空间浪费最小的位置，即浪费地图最少。如果平局，则使用 `bottom_left` 来决定。

#### 可选优化：

所有优化都是在创建 GreedyPacker 实例时作为关键字参数传入的：

###### Wastemap
Skyline 算法有可能丧失对天际线后面的空间的跟踪。这个空间可以使用类似 Shelf 算法的 wastemap 来恢复。强烈建议在使用 Skyline 算法时启用此功能，默认设置为 True。

使用方法：
```
In [15]: M = greedypacker.BinManager(8, 4, 'shelf', 'best_width_fit', wastemap=True)
```
