# 二维装箱

[![Build Status](https://travis-ci.org/ssbothwell/greedypacker.svg?branch=master)](https://travis-ci.org/ssbothwell/greedypacker)
[![Coverage Status](https://coveralls.io/repos/github/ssbothwell/greedypacker/badge.svg?branch=master)](https://coveralls.io/github/ssbothwell/greedypacker?branch=master)

Solomon Bothwell

ssbothwell@gmail.com

![Maximal Rectangle Rendering](https://raw.githubusercontent.com/ssbothwell/greedypacker/master/static/maximal_rectangleAlgorithm-bottom_leftHeuristic.png)

一个基于 Jukka Jylänki 的文章 ["A Thousand Ways to Pack the Bin - A Practical Approach to Two-Dimensional Rectangle Bin Packing."](http://clb.demon.fi/files/RectangleBinPack.pdf) 的二维装箱库。

这个库用于离线装箱。所有来自 Jukka 的文章的算法启发式和优化都已包含在内。

一个使用 Flask 和 ReactJS 制作的Web演示可以在["这里"](https://ssbothwell.github.io/greedypacker-react/)找到。不同的优化组合和数据集会显著影响装箱性能，因此了解设置并测试各种组合非常重要。


### 用法示例:
```
In [1]: import greedypacker

In [2]: M = greedypacker.BinManager(8, 4, pack_algo='shelf', heuristic='best_width_fit', wastemap=True, rotation=True)

In [3]: ITEM = greedypacker.Item(4, 2)

In [4]: ITEM2 = greedypacker.Item(5, 2)

In [5]: ITEM3 = greedypacker.Item(2, 2)

In [6]: M.add_items(ITEM, ITEM2, ITEM3)

In [7]: M.execute()

In [8]: M.bins
Out[8]: [Sheet(width=8, height=4, shelves=[{'y': 2, 'x': 8, 'available_width': 0, 'area': 6, 'vertical_offset': 0, 'items': [Item(width=5, height=2, x=0, y=0)]}, {'y': 2, 'x': 8, 'available_width': 4, 'area': 8, 'vertical_offset': 2, 'items': [Item(width=4, height=2, x=0, y=2)]}])]
```

#### 算法

##### ["Shelf"](https://github.com/ssbothwell/greedypacker/blob/master/docs/shelf.md)
##### ["Guillotine"](https://github.com/ssbothwell/greedypacker/blob/master/docs/guillotine.md)
##### ["Maximal Rectangles"](https://github.com/ssbothwell/greedypacker/blob/master/docs/maximal_rectangles.md)
##### ["Skyline"](https://github.com/ssbothwell/greedypacker/blob/master/docs/skyline.md)


#### 通用可选参数：

所有优化都是在创建 GreedyPacker 实例时作为关键字参数传入的：

##### 物品旋转
可以通过关键字参数 `rotation=False` 禁用物品旋转。

##### 物品预排序
可以根据 "sorting_heuristic" 关键字参数的多种设置对物品进行预排序：

* ASCA: 按面积升序排序
* DESCA: 按面积降序排序（这是默认设置）
* ASCSS: 按较短边升序排序
* DESCSS: 按较短边降序排序
* ASCLS: 按较长边升序排序
* DESCLS: 按较长边降序排序
* ASCPERIM: 按周长升序排序
* DESCPERIM: 按周长降序排序
* ASCDIFF: 按边长差异的绝对值升序排序
* DESCDIFF: 按边长差异的绝对值降序排序
* ASCRATIO: 按边长比例升序排序
* DESCRATIO: 按边长比例降序排序
* False: 按照添加到箱子管理器的顺序进行装箱

##### 算法特定的优化/设置：
请参考上面链接的特定算法页面。

### 安装说明

需要 Python `>=3.0`。

### 测试

```shell
python -m unittest test
```
