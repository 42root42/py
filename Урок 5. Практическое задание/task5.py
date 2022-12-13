with open('files/task5.txt', 'w', encoding='UTF-8') as f:
    nums = input('Введи числа через пробел: ')
    f.writelines(nums)

    l_nums = nums.split()
    num_sum = 0

    for l in l_nums:
        num_sum += int(l)

    print(num_sum)
