n = 17


"""def collatz(a):
    numbers = [a]
    while a != 1:
        if a % 2 == 0:
            a /= 2
            numbers.append(int(a))
        else:
            a = (a * 3) + 1
            numbers.append(int(a))
    return numbers"""


def collatz(a):
    yield a
    while a != 1:
        if a % 2 == 0:
            a /= 2
            yield int(a)
        else:
            a = (a * 3) + 1
            yield int(a)


print(*collatz(n))
