from random import *
word_list = ["тарелка", "пылесос",
             "чердак", "незнайка", "буревестник", "поднос", "спаржа", "крыжовник", "чемпионат",
             "пятновыводитель", "упражнение", "олимпиада", "клавиатура", "подорожник", "черемуха"
             "бардель", "месиво", "календула", "ноябрь", "сентябрь", "пятница", "воскресенье",
             "чебурашка", "покемон", "пикачу", "барбарис", "мартышка", "лягушка", "крестик", "барабан",
             "переворот", "упрощение", "соединение", "облако", "благовещенск", "драгоценность", "шампанское",
             "настойка", "перегородка", "операция", "дуриан", "пальма", "заповедник", "ультразвук",
             "ноутбук", "наручники", "круассан", "молоко", "математика", "биология", "география",
             "грейпфрут", "апельсин", "параллелепипед", "треугольник", "квадрат", "умножение",
             "деление", "разветвлитель"]


def get_word():
    result = choice(word_list).upper()
    return result


def display_hangman(tries):
    stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давайте играть в угадайку слов, у вас есть 6 попыток!")
    print(display_hangman(tries))
    print(word_completion)
    while tries > 0:
        text = input("Введите одну букву или слово   ").upper()
        while not text.isalpha():
            text = input("Может всё таки букву или целое слово?   ").upper()
        while guessed_words.count(text) > 0 or guessed_letters.count(text) > 0:
            text = input("Вы повторяетесь, введите другую букву или слово   ").upper()
        if len(text) == 1:
            guessed_letters.append(text)
            if text in word:
                print("Молодец, есть такая буква в слове!")
                print(display_hangman(tries))
                for i in range(len(word)):
                    if word[i] == text:
                        word_completion = word_completion[:i] + word[i] + word_completion[i + 1:]
                print(word_completion)
                if word_completion == word:
                    print("Поздравляем вы отгадали слово!")
                    guessed = True
                    break
            else:
                tries -= 1
                print("Нет такой буквы в слове")
                print(display_hangman(tries))
                print(word_completion)
        else:
            guessed_words.append(text)
            if text == word:
                print("Поздравляем вы отгадали слово!")
                guessed = True
                break
            else:
                print("Это неверное слово")
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
    if guessed:
        print("Ждём вас снова!")
    else:
        print("Ваши попытки закончились. Game Over")


word_gen = get_word()
play(word_gen)