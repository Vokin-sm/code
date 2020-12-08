numbers = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    lst_2 = l[:]
    for el in lst_2:
        if el % 2 == 1:
            l.remove(el)
        else:
            l[l.index(el)] //= 2


"""def modify_list(l):
    s = [i//2 for i in l if i % 2 == 0]
    l.clear()
    l.extend(s)"""


print(numbers)
modify_list(numbers)
print(numbers)
