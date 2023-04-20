# board = list(range(1, 10))
# wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
#
#
# def board_():
#     print("-------------")
#     for i in range(3):
#         print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
#     print("-------------")
#
#
# def dots(player):
#     while True:
#         value = input('куда поставить ' + player + '?')
#         if not (0 < int(value) < 10):
#             print('ошибочный ввод')
#             continue
#         value = int(value)
#         if str(board[value - 1]) in 'xo':
#             print('клетка уже занята')
#             continue
#         board[value - 1] = player
#         break
#
#
# def win():
#     for w in wins:
#         if (board[w[0] - 1]) == (board[w[1] - 1]) == (board[w[2] - 1]):
#             return board[w[1] - 1]
#     else:
#         return False
#
#
# def main():
#     counter = 0
#     while True:
#         board_()
#         if counter % 2 == 0:
#             dots('x')
#         else:
#             dots('o')
#         if counter > 3:
#             winner = win()
#             if winner:
#                 board_()
#                 print(winner, 'победа')
#                 break
#         counter += 1
#         if counter > 8:
#             board_()
#             print('ничья')
#             break
#
#
# main()

