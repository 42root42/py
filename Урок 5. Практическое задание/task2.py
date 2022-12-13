with open('files/task2.txt', 'r', encoding='UTF-8') as f:
    lstr = f.readlines()
    print(f'В файле {len(lstr)} строк')
    for l in range(len(lstr)):
        print(f'В {l+1} строке {len(lstr[l].split())} слов')
