from typing import List, Any, Union

a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50, "fifth", 56, 67, 87]
f = {}
g = []

for i in range(len(a)):
    if type(a[i]) == str:
        g = []
        f[a[i]] = g
    else:
        g.append(a[i])
print(f)
print()

for element in a:
    if type(element) == str:
        g = []
        f[element] = g
    else:
        g.append(element)
print(f)
print()

my_text = "Привет, пока, велосипед, пока, привет, отпуск, работа, море, дом, пока, отпуск, автомобиль, волны, закат"
a = my_text.split()
print(a)
print(len(a))
print()

b = {}
n = 1
for element in a:
    b[element] = n
    n += 1
print(b)
print(n-1)
print()

c = {}
for word in my_text.split():
    if word in c:
        c[word] += 1
    else:
        c[word] = 1
print(c)
print()

x = {}
for word in my_text.split():
    x[word] = x.get(word, 0) + 1
print(x)














