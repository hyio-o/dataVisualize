import random
import matplotlib.pyplot as plt

squares = []
for value in range(1, 11):
    r_val = int(random.random() * 100)
    squares.append(r_val)

plt.plot(squares, linewidth=2)
plt.show()
