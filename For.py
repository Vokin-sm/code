names = ["Mike", "Tom", "Katy", "Alex", "Sergey"]

for element in names:
    print(element)
print()

for i in range(0, len(names)):
    print(names[i])
print()

for i in range(len(names)):
    for j in range(i+1):
        print(names[i])

