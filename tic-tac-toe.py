# Задаем размеры игрового поля
board = list(range(1, 10))
# Назначаем выигрышные комбинации
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# Рисуем поле
def board_():
    print("-------------")
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print("-------------")


# Пишем функцию для значений (Х и 0) и проверяем правильность ввода
def dots(player):
    while True:
        value = input('куда поставить ' + player + ' ?: ')
        if not (0 < int(value) < 10):
            print('ошибочный ввод')
            continue
        value = int(value)
        if str(board[value - 1]) in 'X0':
            print('клетка уже занята')
            continue
        board[value - 1] = player
        break


# Пишем функцию для определения выигрышных комбинаций
def win():
    for w in wins:
        if (board[w[0] - 1]) == (board[w[1] - 1]) == (board[w[2] - 1]):
            return board[w[1] - 1]
    else:
        return False


# Пмшем основную функцию для игры
def main():
    counter = 0
    while True:
        board_()
        if counter % 2 == 0:
            dots('X')
        else:
            dots('0')
        if counter > 3:
            board_()
            winner = win()
            print(winner, '- победил')
            break
        counter += 1
        if counter > 8:
            board_()
            print('ничья')
            break


main()
