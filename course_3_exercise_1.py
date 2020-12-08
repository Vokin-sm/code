s = "Beautiful is better than ugly. Explicit is better than implicit."
word_list = s.split()
d = dict()

for word in word_list:
    if len(word) not in d.keys():
        d[len(word)] = 1
    else:
        d[len(word)] += 1

for el in sorted(d.keys()):
    print(str(el) + ": " + str(d[el]))