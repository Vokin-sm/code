roman_numbers = {1: "I",
                 4: "IV",
                 5: "V",
                 9: "IX",
                 10: "X",
                 40: "XL",
                 50: "L",
                 90: "XC",
                 100: "C",
                 400: "CD",
                 500: "D",
                 900: "CM",
                 1000: "M"}
number = 1984
roman_number = ""

digit_1 = (number // 1000)
digit_2 = ((number % 1000) // 100) * 100
digit_3 = ((number % 100) // 10) * 10
digit_4 = number % 10


def rom_num(a):
    b = int(str(1) + str((len(str(a)) - 1) * "0"))
    if a == 4 * b or a == 5 * b or a == 9 * b:
        return roman_numbers[a]
    if 0 <= a <= 3 * b:
        return roman_numbers[b] * int((a / b))
    if 5 * b < a < 9 * b:
        return roman_numbers[b * 5] + (roman_numbers[b] * (int((a / b)) - 5))


roman_number += roman_numbers[1000] * digit_1
roman_number += rom_num(digit_2)
roman_number += rom_num(digit_3)
roman_number += rom_num(digit_4)
print(roman_number)
