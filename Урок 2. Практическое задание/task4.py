words = input('Введи слова через пробел: ')

for ind, w in enumerate(words.split(' '), 1):
    print(f'{ind}. {w[:10]}')