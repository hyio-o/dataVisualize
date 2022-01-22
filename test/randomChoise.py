from random import choice

squares = list(range(1, 10))
x_val = choice(squares)
while x_val != 5:
    print(choice(squares), "  ", end='')
    x_val = choice(squares)


