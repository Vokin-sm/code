word_1 = "silent".lower()
word_2 = "listen".lower()
flag = True


if len(word_1) == len(word_2):
    for letter in word_1:
        if letter not in word_2:
            flag = False
        if word_1.count(letter) != word_2.count(letter):
            flag = False
else:
    flag = False

if flag:
    print(True)
else:
    print(False)
