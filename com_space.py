#! /usr/bin/python3

import sys
import time
import copy

'''
EXAMPLE CLASS
class SaveState:
    def __init__(self, ordered, possibilities, board):
        self.ordered = ordered
        self.possibilities = possibilities
        self.board = board

    def print_state(self):
        print("Print_state. index: %d"%self.ordered[-1])
        printBoard("board: ", self.board)
'''
#thanks mr. brooks
#globals
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# Transformations (rotations are counter-clockwise)
Rot90 = [6,3,0,7,4,1,8,5,2]
Rot180 = [8,7,6,5,4,3,2,1,0]
Rot270 = [2,5,8,1,4,7,0,3,6]
VertFlip= [2,1,0,5,4,3,8,7,6]
Transformations = [[Rot90],[Rot180],[Rot270],[VertFlip],[Rot90,VertFlip],[Rot180,VertFlip],[Rot270,VertFlip]]

def isWinning(board):
    global wins
    for group in wins:
        if board[group[1]] != -1 and board[group[0]] == board[group[1]] and board[group[1]] == board[group[2]]:
            return True
    return False

def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
'''
A) Calculate the number of different possible games.
Two games are different if the Nth move in each game is different,
for at least one value of N.
'''
#we're saying 1 is x and 0 is o
def A():
    total_games = 0
    for x1 in range(9):
        board9 = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        still_avail9 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        still_avail9.remove(x1)
        print("filling in space %d with x, remaining spaces:"%x1)
        print(still_avail9)
        still_avail8 = still_avail9[:]
        board9[x1] = 1
        for o1 in still_avail8:
            board8 = board9[:]
            still_avail8.remove(o1)
            still_avail7 = still_avail8[:] #is this ok? i just don't want seperate trees affecting each other
            print("filling in space %d with o, remaining spaces:"%o1)
            print(still_avail8)
            board8[o1] = 0
            for x2 in still_avail7:
                board7 = board8[:]
                still_avail7.remove(x2)
                still_avail6 = still_avail7[:] #is this ok? i just don't want seperate trees affecting each other
                print("filling in space %d with x, remaining spaces:"%x2)
                print(still_avail7)
                board7[x2] = 1
                for o2 in still_avail6:
                    board6 = board7[:]
                    still_avail6.remove(o2)
                    still_avail5 = still_avail6[:] #is this ok? i just don't want seperate trees affecting each other
                    print("filling in space %d with o, remaining spaces:"%o2)
                    print(still_avail6)
                    board6[o2] = 0
                    #have to start checking for wins now cuz there are 3
                    for x3 in still_avail5:
                        board5 = board6[:]
                        still_avail5.remove(x3)
                        still_avail4 = still_avail5[:] #is this ok? i just don't want seperate trees affecting each other
                        print("filling in space %d with x, remaining spaces:"%x3)
                        print(still_avail5)
                        board5[x3] = 1
                        if isWinning(board5):
                            print_board(board5)
                            total_games+=1
                        else:
                            for o3 in still_avail4:
                                board4 = board5[:]
                                still_avail4.remove(o3)
                                still_avail3 = still_avail4[:] #is this ok? i just don't want seperate trees affecting each other
                                print("filling in space %d with o, remaining spaces:"%o3)
                                print(still_avail4)
                                board4[o3] = 0
                                if isWinning(board4):
                                    print_board(board4)
                                    total_games+=1
                                else:
                                    for x4 in still_avail3:
                                        board3 = board4[:]
                                        still_avail3.remove(x4)
                                        still_avail2 = still_avail3[:]
                                        print("filling in space %d with x, remaining spaces:"%x4)
                                        print(still_avail3)
                                        board3[x4] = 1
                                        if isWinning(board3):
                                            print_board(board3)
                                            total_games+=1
                                        else:
                                            #i'm confused for this part. in reality when there are 2 spaces left,
                                            #there are 2 more board possible. you can put o one place, and  it either wins
                                            #or leads to putting down an x and that's a full board so either way that's +1.
                                            #or you put the o in the other place, and that wins or again you just put x in the other
                                            #place and that's +1 too. so from here there are 2 more boards and
                                            #that's that
                                            total_games+=2
    return total_games
'''
B) In how many of the total number of games:
B-1) was a win by X?
B-2) was a win by O?
B-3) was a draw?
'''
def B1():
    return 0
def B2():
    return 0
def B3():
    return 0
'''
C) Calculate the number of different possible board configurations
in all possible games (not just final boards at ends of games,
but all intermediate boards). Include the blank (beginning) board.
'''
def C():
    return 0
'''
D) Most boards in C) above are reducible to other boards.
Calculate the number of irreducible board families.
All the boards to the right are reducible to each other via
rotations of 90, 180 and 270 degrees, or a mirror flip plus a
possible added rotation by 90, 180 or 270 degrees
'''
def D():
    return 0

def main():
    print("A: %d"%A())
    print("B1: %d"%B1())
    print("B2: %d"%B2())
    print("B3: %d"%B3())
    print("C: %d"%C())
    print("D: %d"%D())

main()
