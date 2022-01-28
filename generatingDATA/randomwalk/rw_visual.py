import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
# plt.scatter(rw.x_value, rw.y_value, s=1)
# 着色
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10)
# 起点与终点
plt.scatter(0, 0, c='green', edgecolors='black', s=100)
plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='black', s=100)
# 隐藏坐标轴
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

plt.show()
