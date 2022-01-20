import matplotlib.pyplot as plt  # 导入了模块pyplot ，并给它指定了别名plt ，以免反复输入pyplot ；；模块pyplot 包含很多用于生成图表的函数
import matplotlib as mpl
import numpy as np


#squares = [1, 4, 9, 16, 25]
squares = []
for value in range(1, 2**8):
    square = value**2;
    squares.append(square)
plt.plot(squares)  # 创建了一个列表，在其中存储了前述平方数，再将这个列表传递给函数plot()
plt.show()  # plt.show() 打开matplotlib查看器，并显示绘制的图形
