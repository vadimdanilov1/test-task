numbers1 = ['R', 'G', 'B', 'W']
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers3 = []
order1 = []
order2 = []
fin = True

for i in range(len(numbers1)):
    for j in range(len(numbers2)):
        numbers3.append(numbers1[i] + str(numbers2[j]))

print('Введите команду "start N C" для раздачи N случайных карт, С игрокам')

while fin:
    order1 = input().split()
    n = int(order1[1])
    c = int(order1[2])

    if n * c > 40:
      print('ВНИМАНИЕ! Карт в колоде всего 40 штук. Карт на всех игроков не хватит. Раздайте ещё раз.')
    elif order1[0] != 'start':
        print('ВНИМАНИЕ! Команада "start" введена неверно . Введите команду ещё раз.')
    else:
        fin = False

fin = True
print('Введите команду "get-cards C" для раздачи карт игроку, где С - номер игрока')

while fin:
    order2 = input().split()
    c_number = int(order2[1])
    if c_number > c:
        print('ВНИМАНИЕ! Номер игрока больше, чем общее количество игроков. Введите команду еще раз.')
    elif order2[0] != 'get-cards':
        print('ВНИМАНИЕ! Команада "get-cards" введена неверно . Введите команду ещё раз.')
    else:
        fin = False