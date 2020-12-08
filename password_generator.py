from random import *
digits = "0123456789"
lowercase_letters = "qwertyuioplkjhgfdsazxcvbnm"
uppercase_letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
punctuation = "!#$%&*+-=?@^_."
sim = "i1lLo0O"
chars = ""


def is_valid(text):
    while text.strip() != "да" and text.strip() != "нет":
        text = input("Введите да/нет   ")
    return True


number_of_passwords = int(input("Введите количество необходимых паролей   "))
print()
password_length = int(input("Введите необходимую длину пароля   "))
print()
digits_yn = input("Включать в пароль цифры? (да/нет)   ")
if is_valid(digits_yn):
    if digits_yn.strip() == "да":
        chars += digits
print()
lowercase_letters_yn = input("Включать в пароль строчные буквы? (да/нет)   ")
if is_valid(lowercase_letters_yn):
    if lowercase_letters_yn.strip() == "да":
        chars += lowercase_letters
print()
uppercase_letters_yn = input("Включать в пароль заглавные буквы? (да/нет)   ")
if is_valid(uppercase_letters_yn):
    if uppercase_letters_yn.strip() == "да":
        chars += uppercase_letters
print()
punctuation_yn = input("Включать в пароль знаки? (да/нет)   ")
if is_valid(punctuation_yn):
    if punctuation_yn.strip() == "да":
        chars += punctuation
print()
sim_yn = input("Исключить из пароля неоднозначные символы i1lLo0O? (да/нет)   ")
if is_valid(digits_yn):
    if sim_yn.strip() == "да":
        for c in sim:
            chars = chars.replace(c, "")
print()


def generate_password(length, chars):
    result = ""
    for _ in range(length):
        result += choice(chars)
    return result


for _ in range(number_of_passwords):
    print(generate_password(password_length, chars))
