import math
from fractions import Fraction

numbers = "239/30".split("/")
x = Fraction(int(numbers[0]), int(numbers[1]))
a_0 = math.floor(x)
elements = [a_0]
x_n = x - a_0

while True:
    a_n = math.floor(1 / x_n)
    elements.append(a_n)
    x_n = (1 / x_n) - a_n
    if x_n == 0:
        break

print(*elements)
