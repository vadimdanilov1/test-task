import random

numbers1 = ['R', 'G', 'B', 'W']
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers3 = []
order1 = []
order2 = []
cards = []
players = []
fin = True

for i in range(len(numbers1)):
    for j in range(len(numbers2)):
        numbers3.append(numbers1[i] + str(numbers2[j]))

print('Введите команду "start N C" для раздачи N случайных карт, С игрокам')
n = 0
c = 0
while fin:
    order1 = input().split()
    n = int(order1[1])
    c = int(order1[2])

    if order1[0] != 'start':
        print('ВНИМАНИЕ! Команада "start" введена неверно . Введите команду ещё раз.')
    elif n * c > 40:
        print('ВНИМАНИЕ! Карт в колоде всего 40 штук. Карт на всех игроков не хватит. Раздайте ещё раз.')
    else:
        fin = False

again = 'y'
while again.lower() == 'y':
    fin = True
    print('Введите команду "get-cards C" для раздачи карт игроку, где С - номер игрока')
    while fin:
        order2 = input().split()
        c_number = order2[1]
        if order2[0] != 'get-cards' or len(order2) != 2:
            print('ВНИМАНИЕ! Команада "get-cards" введена неверно . Введите команду ещё раз.')
        elif int(c_number) > c:
            print('ВНИМАНИЕ! Номер игрока больше, чем общее количество игроков. Введите команду еще раз.')
        elif int(c_number) in players:
            print('Этому игроку карты уже раздавались. Введите команду ещё раз.')
        else:
            players.append(int(c_number))
            fin = False

    cards = list()
    for i in range(n):
        cards.append(numbers3[random.randrange(len(numbers3))])
        numbers3.remove(cards[i])

    cards.insert(0, order2[1])
    print(*cards)

    if len(numbers3) < n:
        print('Карт для раздачи больше не осталось')
        break
    again = input('Раздать ещё? (y = yes, n = no):  ')

print('Карты розданы')
print('Оставшиеся карты в колоде:', *numbers3)
print('Количество оставшихся к колоде карт:', len(numbers3))
