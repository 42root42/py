repl = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
ru_nums = []

with open('files/task4_en.txt', 'r', encoding='UTF-8') as f:
    with open('files/task4_ru.txt', 'w', encoding='UTF-8') as f_ru:
        for l in f:
            l = l.split(' ', 1)
            ru_nums.append(repl[l[0]] + ' ' + l[1])

        f_ru.writelines(ru_nums)
