from functools import reduce


def my_func(one, two):
    return one * two


even_list = [x for x in range(100, 1001, 2)]
print(even_list)

print(reduce(my_func, even_list))
