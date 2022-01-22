import random
import matplotlib.pyplot as plt

# squares = []
"""for value in range(1, 2**4):
    x_val = int(random.random() * 100)
    y_val = int(random.random() * 100)
    plt.scatter(x_val, y_val, s=100)
"""
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)
plt.axis([0, 1100, 0, 1100000])

print(x_values)
print(y_values)

# plt.scatter(2, 4)
plt.show()
