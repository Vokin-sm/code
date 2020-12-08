a = set()
print(a)

a = set([1, 5, 10, 'hello'])
print(a)

b = {1, 10, 'hello', 'hey'}
print(b)

c = {1, 5, 8, 10}
print(type(c))

a = set()
a.add(1)
print(a)
a.add(25)
print(a)
a.add('Hello')
a.add(2)
a.add(10)
print(a)
a.add(25)
print(a)

for el in a:
    print(el)

my_list = [1, 2, 2, 5, 6, 5, 'hello', 'hey', 'hello']
my_set = set(my_list)
print(my_set)
my_list = list(my_set)
print(my_list)

a = {'hello', 'hey', 1, 10, 5}
print(5 in a)
print('hey' in a)
print(3 in a)
print(15 not in a)
print(a)

my_list = [1, 1, 2, 5, 5, 10, 10, 10]
total = 0
for num in set(my_list):
    total += num
print(total)

print(sum(set(my_list)))


def my_func(input_set, input_list):
    if len(input_list) > len(input_set):
        return False
    for list_el in input_list:
        if list_el not in input_set:
            return False
    return True


print(my_func({1, 2, 3, 4, 5, }, [1, 2, 3, 4, 6]))





my_func(input_set, input_list)


