#  模拟骰子
from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides      # 被定义6面将值传递给类中方法-初始化面数

    def roll(self):
        return randint(1, self.num_sides)   # 随机选择1 -> self.num_sides 中的任意一个数字； randint函数
