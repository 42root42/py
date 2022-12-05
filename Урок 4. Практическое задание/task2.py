src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

gen_list = [src_list[num] for num in range(1, len(src_list)) if src_list[num] > src_list[num - 1]]

print(gen_list)