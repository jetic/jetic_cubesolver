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
# 2017/10/27
+ 采用表的方式记录各状态的转换关系
+ 包括角位置表(43200)，角方向表(2187)，棱方向表(2048)
+ 棱位置表规模太大，还在思考实现方法(479001600)
+ 已经在现实中成功解开了Oskar3*3魔方，因此本项目目标发生了变化：建模解Oskar => 3*3*3 cube solver 优化