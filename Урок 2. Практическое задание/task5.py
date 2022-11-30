rating = [9, 7, 6, 5, 5, 4, 1]

print(f'Текущий рейтинг: {rating}')

while True:
    x = input('Введи число или stop для выхода: ')
    if x == 'stop':
        print(f'Итоговый рейтинг: {rating}')
        break

    else:
        rating.append(int(x))
        rating.sort(reverse=True)
        print(f'Новый рейтинг: {rating}')