### Maximal Rectangles 算法
  ![Maximal Rectangle 渲染](https://raw.githubusercontent.com/ssbothwell/greedypacker/master/static/maximal_rectangleAlgorithm-bottom_leftHeuristic.png)

  与 Guillotine 算法中选择切割轴不同，Maximal Rectangles 将两种可能的切割都添加到 FreeRectangles 列表中。这确保了在任何时候 FreeRectangles 列表中都包含了最大可能的矩形区域。

  由于现在箱子中的单个点可以由多个 FreeRectangles 表示，所以必须在物品插入之间仔细修剪列表。任何与新插入的物品占用区域相交的 FreeRectangle 都会被拆分以消除交集。此外，任何完全被另一个 FreeRectangle 覆盖的 FreeRectangle 都会从列表中删除。

  ```
  M = greedypacker.BinManager(8, 4, pack_algo='maximal_rectangle', heuristic='bottom_left', rotation=True)
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
* bottom_left:
  选择一个 FreeRectangle，其中物品顶边的Y坐标最小。如果平局，选择X坐标较小的选项。
* contact_point:
  选择一个 FreeRectangle，其中物品周长的最大部分与已占用空间或箱子的边缘接触。如果平局，则使用 `best_shortside` 来决定。
