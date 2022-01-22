from random import choice

"""“”“为做出随机决策，我们将所有可能的选择都存储在一个列表中，并在每次做决策时都使用choice() 来决定使用哪种选择（见❶）”“”"""


class RandomWalk():
    # 生成随机漫步数据
    def __init__(self, num_points=5000):  # 初始化
        self.num_points = num_points
        self.x_value = [0]  # 所有随机漫步 起始 与 原点
        self.y_value = [0]

    def fill_walk(self):  # 计算随机漫步所包含的所有点
        while len(self.x_value) < self.num_points:  # 漫步至指定长度
            x_direction = choice([1. -1])  # 决定前进方向以及沿这个方向前进的距离, 随机选择 1 或者 -1
            x_distance = choice({0, 1, 2, 3, 4})
            x_step = x_direction * x_distance

            y_direction = choice([1. -1])
            y_distance = choice({0, 1, 2, 3, 4})
            y_step = y_direction * y_distance
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x y值  _value[-1] 应该指的是数列最末尾一位
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
