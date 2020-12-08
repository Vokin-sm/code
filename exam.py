my_set = set()
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):

                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
                    my_set.add(a ** 3 + b ** 3)
my_list = list(my_set)
my_list = sorted(my_list)
print(my_list)
