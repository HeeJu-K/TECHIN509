# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random
import csv

class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        #function to print out the board
        s = '\n'
        s += "  a b c\n"
        i = 0
        for row in self._rows:
            s+=str(i)
            i += 1
            for cell in row:
                s = s+'|'
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
                # s = s+'|'
            s = s+'|\n'
        return s
    
    def get(self, x, y):
        return self._rows[x][y]
    
    def set(self, x, y, value):
        self._rows[x][y] = value

    def get_winner (self): 
        check_diag_0 = str(self._rows[0][0]) + str(self._rows[1][1]) + str(self._rows[2][2])
        check_diag_1 = str(self._rows[0][2]) + str(self._rows[1][1]) + str(self._rows[2][0])
        for i in range (0, 3): 
            check_hor = str(self._rows[i][0]) + str(self._rows[i][1]) + str(self._rows[i][2])
            check_ver = str(self._rows[0][i]) + str(self._rows[1][i]) + str(self._rows[2][i]) 
            if check_hor == 'OOO' or check_ver == 'OOO': 
                return "O"
            if check_hor == 'XXX' or check_ver == 'XXX':
                return "X"
        if check_diag_0 == 'OOO' or check_diag_1 == 'OOO':
            return "O"
        if check_diag_0 == 'XXX' or check_diag_1 == 'XXX':
            return "X"
        #when no winners
        return None
    
    def writeRank (self, player_id, winner):

        data = [ player_id, winner ]
        
        with open('Rank.csv', 'a') as csvfileW:
            rankWriter = csv.writer(csvfileW)
            rankWriter.writerow(data)
            csvfileW.close()
        return
    
    def showRank (self):
        ranking_board = {}
        with open ("Rank.csv") as csvfileR:
            rankReader = csv.reader(csvfileR)
            for row in rankReader:
                if not row[0] in ranking_board:
                    ranking_board[row[0]] = [0, 0, 0, 0] # these datas in turn are total score, # of games won, drawn and lost
                if row[1] == 'X': #this is when the game is won
                    ranking_board[row[0]][1] += 1
                    ranking_board[row[0]][0] += 1
                elif row[1] == 'O': #this is when the game is lost
                    ranking_board[row[0]][2] += 1
                    ranking_board[row[0]][0] -= 1
                elif row[1] == None:
                    ranking_board[row[0]][1] += 1
            # print(ranking_board)
        #sort
        sorted_ranking = sorted(ranking_board.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_ranking)
        print("----------------\nGlobal Ranking: \n----------------\nPlayer ID | Score\n")
        for row in sorted_ranking:
            print(" ", row[0], " | ", row[1][0], "\n")
        return

class Game:
    def __init__(self, player_X, player_O):
        self.board = Board()
        self.player_X = player_X
        self.player_X.symbol = 'X'
        self.player_O = player_O
        self.player_O.symbol = 'O'
        self.current_player = 'O'
    
    def get_next_player(self):
        if self.current_player == 'O':
            self.current_player = 'X'
            return self.player_X
        else :
            self.current_player = 'O'
            return self.player_O
    
    def run(self):
        #runs and controls the game, identifies which player and when to terminate game
        winner = self.board.get_winner()
        count = 0
        while winner == None and count !=9:
            #continue game if there's no winner yet and board is not full
            next_player = self.get_next_player()
            next_player.get_move(self.board)
            winner = self.board.get_winner()
            count += 1 
        if winner == None:
            print("there is no winner")
        else:
            print("winner is :" + winner)
        return winner

class Human:
    def __init__(self, symbol):
        self.symbol = symbol
    def get_move(self, board):
        while True:
            #check if it's a legal position before placing
            print(board.__str__())

            x = int(input("enter row coordinate :" ))
            y = input("enter col coordinate :" )
            # y = input("enter y coordinate :" )
            if y == "a":
                y = 0
            elif y == "b":
                y = 1
            elif y == "c":
                y = 2
            if x<0 or x>2 or y<0 or y>2:
                print("coordinate is out of range")
                continue
            else:
                if board.get(x, y) == None:
                    board.set(x, y, self.symbol)
                    break
                else:
                    print("already taken")

class Bot:
    def __init__(self, symbol):
        self.symbol = symbol
    def get_move(self, board):
        while True:
            x = random.randint(0,2)
            y = random.randint(0,2)
            if board.get(x, y) == None:
                board.set(x, y, self.symbol)
                print(board.__str__())
                break
            else:
                print("already taken")


