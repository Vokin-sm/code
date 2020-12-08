roman_number = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000}
number = 0
s = input("Введите римское число   ")
print(s)
s = [roman_number[i] for i in list(s)]

for i in range(len(s) - 1):
    if s[i] >= s[i + 1]:
        number += s[i]
    else:
        number -= s[i]

number += s[-1]
print(number)
