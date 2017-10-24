## jetic_cubesolver
Solve puzzle. Bought a Oskar 3*3 and I can't solve it. So I want to find solutions of different kinds of puzzles.

## Update list：
# 2017/10/23
+ 开始cube solver
+ 3*3的用R和U操作进行的从指定状态复原
+ 已经支持了所有的URFDLB操作，BFS查找
# 2017/10/24
+ 修复了B操作角块错误的bug
+ 从初始态和最终态两边同时BFS，节省一半深度
+ 可以选择性采用18种操作中的部分操作，寻找指定变换群上的解