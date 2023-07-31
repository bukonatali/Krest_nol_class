board = list(range(1, 10))


def draw_board(board):
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")


class Kr_nol:
    def __init__(self, board):
        self.board = board

    def take_input(self,player_1):
        valid = False
        while not valid:
            player_2 = input("Игрок, куда поставим " + player_1 + "? ")
            try:
                player_2 = int(player_2)
            except:
                print("Некорректный ввод. Введите число?")
                continue
            if player_2 >= 1 and player_2 <= 9:
                if (str(board[player_2 - 1]) not in "X", "O"):
                    board[player_2 - 1] = player_1
                    valid = True
                else:
                    print("Это место уже занято")
            else:
                print("Некорректно. Введите число от 1 до 9 .")

    def check_win(self, board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False


    def main(self):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                self.take_input("X")
            else:
                self.take_input("O")
            counter += 1
            if counter > 4:
                tmp = self.check_win(board)
                if tmp:
                    print(tmp, "Победил!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)


if __name__ == '__main__':
    Kr_nol(board).main()
