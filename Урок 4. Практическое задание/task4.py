src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
gen_list = [num for num in src_list if src_list.count(num) == 1]

print(gen_list)
