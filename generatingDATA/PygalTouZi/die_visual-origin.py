import pygal

from die import Die  # 此为die文件

die = Die()  # 此为die变量
results = []
for roll_num in range(2**20):
    result = die.roll()
    results.append(result)

# print(results)
# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):  # 1->6  == value
    frequency = results.count(value)  # .count(*) 为计算出现次数的函数，一个方法｜写好的轮子
    frequencies.append(frequency)
    print("[", value, "]==", frequency, end='\t')

hist = pygal.Bar()  # 统计图， 条形图📊

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')   # TODO 这种文件的扩展名必须为.svg
