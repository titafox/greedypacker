### Shelf 算法
  ![Shelf 渲染](https://raw.githubusercontent.com/ssbothwell/greedypacker/master/static/shelfAlgorithm-next_fitHeuristic.png)

  将箱子划分为高度与第一个插入的物品相等的水平行。将这些行记录在一个列表中，并使用所需的启发式方法选择一行。

  示例代码：
  ```
  M = greedypacker.BinManager(8, 4, pack_algo='shelf', heuristic='best_width_fit', wastemap=True, rotation=True)
  ```

#### 启发式选择：
* next_fit:
  检查当前打开的货架，如果物品适合，则插入。否则创建一个新的货架并关闭以前的货架。
* first_fit:
  循环遍历所有的货架或 FreeRectangles，并将物品放入第一个适合的货架。
* best_width_fit:
  将物品放入会导致剩余空闲宽度最小的货架或 FreeRectangle 中。
* best_height_fit:
  将物品放入会导致剩余空闲高度最小的货架或 FreeRectangle 中。
* best_area_fit:
  将物品放入会导致剩余空闲面积最小的货架或 FreeRectangle 中。
* worst_width_fit:
  将物品放入会导致剩余空闲宽度最大的货架或 FreeRectangle 中。
* worst_height_fit:
  将物品放入会导致剩余空闲高度最大的货架或 FreeRectangle 中。
* worst_area_fit:
  将物品放入会导致剩余空闲面积最大的货架或 FreeRectangle 中。

#### 可选优化：

所有优化都是在创建 GreedyPacker 实例时作为关键字参数传入的：

###### Wastemap
将高度不同的物品放在货架上会导致许多浪费空间，位于每个物品上方的空间都被浪费了。这个优化使用 Guillotine 算法来跟踪这些浪费的区域，并尝试将物品插入其中。每当一个物品无法适应现有的货架并在创建新货架之前，浪费地图都会被更新。

使用方法：
```
M = greedypacker.BinManager(8, 4, 'shelf', 'best_width_fit', wastemap=True)
```
