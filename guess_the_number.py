from random import *
number = randint(1, 100)
count = 0
print("Добро пожаловать в числовую угадайку")


def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
    return False


while True:
    n = input("Введите целое число от 1 до 100   ")
    if is_valid(n):
        n = int(n)
        if n < number:
            print("Ваше число меньше загаданного, попробуйте ещё разок")
            print()
            count += 1
        elif n > number:
            print("Ваше число больше загаданного, попробуйте ещё разок")
            print()
            count += 1
        else:
            print("Вы угадали за", count + 1, " попыток, поздравляем!")
            again = input("Введите Enter, если хотите сыграть ещё раз!")
            print()
            if again == "":
                count = 0
                number = randint(1, 100)
                continue
            else:
                break
    else:
        print("А может всё таки введём целое число от 1 до 100?")

