import random
import os

class ticTacToe:
    def __init__(self) -> None:
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def print_board(self):
        print("")
        print(f"{self.board[0][0]}  |  {self.board[0][1]}  |  {self.board[0][2]}")
        print('-------------')
        print(f"{self.board[1][0]}  |  {self.board[1][1]}  |  {self.board[1][2]}")
        print('-------------')
        print(f"{self.board[2][0]}  |  {self.board[2][1]}  |  {self.board[2][2]}")
    
    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}

        for i in ['X', 'O']:
            # Horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            # Verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i)
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            # Diagonais
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i)
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

        if dict_win['X']:
            self.done = 'x'
            print('X venceu.')
            return
        elif dict_win['O']:
            self.done = 'o'
            print('O venceu.')
            return
        
        c = 0

        for i in range(3):
            for j in range(3):
                if self.board != " ":
                    c += 1
                    break
        if c == 0:
            self.done = 'd'
            print('Empate.')

    def get_player_move(self):
        invalid_mode = True

        while invalid_mode:
            try:
                print('Digite a linha do seu próximo lance: ')
                x = int(input())

                print('Digite a coluna do seu próximo lance: ')
                y = int(input())

                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas inválidas.')
                if self.board[x][y] != " ":
                    print('Posição já preenchida.')
                    continue
            except Exception as e:
                print(e)
                continue
            
            invalid_mode = False
            self.board[x][y] = 'x'

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i,j))
        if len(list_moves) > 0:
            x,y = random.choice(list_moves)
            self.board[x][y] = 'O'

tic = ticTacToe()
tic.print_board()
next = 0

while next == 0:
    os.system('cls')
    tic.print_board()
    while tic.done == '':
        tic.get_player_move()
        tic.make_move()
        os.system('cls')
        tic.print_board()
        tic.check_win_or_draw()


    print('Digite 1 para sair ou qualquer tecla para jogar novamente.')

    next = (input())

    if next == 1:
        break
    else:
        tic.reset()
        next = 0