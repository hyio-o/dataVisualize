import matplotlib.pyplot as plt  # 导入了模块pyplot ，并给它指定了别名plt ，以免反复输入pyplot ；；模块pyplot 包含很多用于生成图表的函数
import matplotlib as mpl
import numpy as np

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,input_values, squares, linewidth=5)

# title
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# scale size
plt.tick_params(axis='x', labelsize=14)

plt.show()
