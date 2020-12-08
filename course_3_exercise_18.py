s = "a aa abC aa ac abc bcd a".lower().split()
words = dict()

for word in s:
    if word not in words.keys():
        words[word] = 1
    else:
        words[word] += 1

[print(el, words[el]) for el in words]
