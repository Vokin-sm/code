number = int(input())


def number_systems(num):
    result = 0
    for i in range(len(num)):
        if num[i].isalpha():
            if num[i] == "A":
                n = 10
                result += n * 16 ** ((len(num) - 1) - i)
            if num[i] == "B":
                n = 11
                result += n * 16 ** ((len(num) - 1) - i)
            if num[i] == "C":
                n = 12
                result += n * 16 ** ((len(num) - 1) - i)
            if num[i] == "D":
                n = 13
                result += n * 16 ** ((len(num) - 1) - i)
            if num[i] == "E":
                n = 14
                result += n * 16 ** ((len(num) - 1) - i)
            if num[i] == "F":
                n = 15
                result += n * 16 ** ((len(num) - 1) - i)
        else:
            result += int(num[i]) * 16 ** ((len(num) - 1) - i)
    return result


def num_sys_from_10_to_16(num):
    num = int(num)
    result = []
    total = ""
    while num > 16:
        result.append(num % 16)
        num //= 16
    result.append(num)
    result = result[::-1]
    for i in range(len(result)):
        if result[i] > 9:
            if result[i] == 10:
                result[i] = "A"
            if result[i] == 11:
                result[i] = "B"
            if result[i] == 12:
                result[i] = "C"
            if result[i] == 13:
                result[i] = "D"
            if result[i] == 14:
                result[i] = "E"
            if result[i] == 15:
                result[i] = "F"
    for i in result:
        total += str(i)
    return total


def num_sys_from_10_to_2(num):
    num = int(num)
    result = []
    total = ""
    while num > 1:
        result.append(num % 2)
        num //= 2
    result.append(num)
    result = result[::-1]
    for i in result:
        total += str(i)
    return total


print(num_sys_from_10_to_16(number))








