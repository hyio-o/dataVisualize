import random
import matplotlib.pyplot as plt

squares = []
for value in range(1, 2**4):
    x_val = int(random.random() * 100)
    y_val = int(random.random() * 100)
    plt.scatter(x_val, y_val, s=100)

plt.axis([0, 110, 0, 110])
# plt.scatter(2, 4)
plt.show()
