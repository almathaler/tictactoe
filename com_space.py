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


def isWinning(board):
    global wins
    for group in wins:
        if board[group[1]] != '_' and board[group[0]] == board[group[1]] and board[group[1]] == board[group[2]]:
            return True
    return False

def print_board(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    print()


'''
A) Calculate the number of different possible games.
Two games are different if the Nth move in each game is different,
for at least one value of N.
'''
#we're saying 1 is x and 0 is o
def A():
    total_games = 0
    total_boards = set()
    o_wins = 0
    x_wins = 0
    draws = 0
    for x1 in range(9):
        board9 = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        still_avail9 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #print("filling in space %d with x, remaining spaces:"%x1)
        #print(still_avail9)
        still_avail8 = still_avail9[:]
        still_avail8.remove(x1)
        board9[x1] = 'x'
        #so we can add to a set
        sb9 = ''.join(board9)
        total_boards.add(sb9)
        for o1 in still_avail8:
            board8 = board9[:]
            still_avail7 = still_avail8[:] #is this ok? i just don't want seperate trees affecting each other
            still_avail7.remove(o1)
            #print("filling in space %d with o, remaining spaces:"%o1)
            #print(still_avail8)
            board8[o1] = 'o'
            #so we can add to a set
            sb8 = ''.join(board8)
            total_boards.add(sb8)
            for x2 in still_avail7:
                board7 = board8[:]
                still_avail6 = still_avail7[:] #is this ok? i just don't want seperate trees affecting each other
                still_avail6.remove(x2)
                #print("filling in space %d with x, remaining spaces:"%x2)
                #print(still_avail7)
                board7[x2] = 'x'
                #so we can add to a set
                sb7 = ''.join(board7)
                total_boards.add(sb7)
                for o2 in still_avail6:
                    board6 = board7[:]
                    still_avail5 = still_avail6[:] #is this ok? i just don't want seperate trees affecting each other
                    still_avail5.remove(o2)
                    #print("filling in space %d with o, remaining spaces:"%o2)
                    #print(still_avail6)
                    board6[o2] = 'o'
                    #so we can add to a set
                    sb6 = ''.join(board6)
                    total_boards.add(sb6)
                    #have to start checking for wins now cuz there are 3
                    for x3 in still_avail5:
                        board5 = board6[:]
                        still_avail4 = still_avail5[:] #is this ok? i just don't want seperate trees affecting each other
                        still_avail4.remove(x3)
                        #print("filling in space %d with x, remaining spaces:"%x3)
                        #print(still_avail5)
                        board5[x3] = 'x'
                        #so we can add to a set
                        sb5 = ''.join(board5)
                        total_boards.add(sb5)
                        if isWinning(board5):
                            #print("x won\n")
                            #print_board(board5)
                            total_games+=1
                            x_wins+=1
                        else:
                            for o3 in still_avail4:
                                board4 = board5[:]
                                still_avail3 = still_avail4[:] #is this ok? i just don't want seperate trees affecting each other
                                still_avail3.remove(o3)
                                #print("filling in space %d with o, remaining spaces:"%o3)
                                #print(still_avail4)
                                board4[o3] = 'o'
                                #so we can add to a set
                                sb4 = ''.join(board4)
                                total_boards.add(sb4)
                                if isWinning(board4):
                                    #print("o won\n")
                                    #print_board(board4)
                                    total_games+=1
                                    o_wins+=1
                                else:
                                    for x4 in still_avail3:
                                        board3 = board4[:]
                                        still_avail2 = still_avail3[:]
                                        still_avail2.remove(x4)
                                        #print("filling in space %d with x, remaining spaces:"%x4)
                                        #print(still_avail3)
                                        board3[x4] = 'x'
                                        #so we can add to a set
                                        sb3 = ''.join(board3)
                                        total_boards.add(sb3)
                                        if isWinning(board3):
                                            #print("x won\n")
                                            #print_board(board3)
                                            total_games+=1
                                            x_wins+=1
                                        else:
                                            for o4 in still_avail2:
                                                board2 = board3[:]
                                                still_avail1 = still_avail2[:]
                                                still_avail1.remove(o4)
                                                board2[o4] = 'o'
                                                #so we can add to a set
                                                sb2 = ''.join(board2)
                                                total_boards.add(sb2)
                                                if isWinning(board2):
                                                    #print("o won\n")
                                                    #print_board(board2)
                                                    total_games+=1
                                                    o_wins+=1
                                                else: #'x5'
                                                    #this is the last x that you're adding. oh we should check if this is a winn
                                                    board2[still_avail1[0]] = 'x'
                                                    #so we can add to a set
                                                    sb2 = ''.join(board2)
                                                    total_boards.add(sb2)
                                                    if isWinning(board2):
                                                        #print("x won\n")
                                                        #print_board(board2)
                                                        x_wins+=1
                                                    else:
                                                        draws+=1
                                                    total_games+=1

                                            #i'm confused for this part. in reality when there are 2 spaces left,
                                            #there are 2 more board possible. you can put o one place, and  it either wins
                                            #or leads to putting down an x and that's a full board so either way that's +1.
                                            #or you put the o in the other place, and that wins or again you just put x in the other
                                            #place and that's +1 too. so from here there are 2 more boards and
                                            #that's that
                                            #total_games+=2

                                            #gotta elaborate for b3 and b2
    return total_games, x_wins, o_wins, draws, len(total_boards), total_boards
'''
B) In how many of the total number of games:
B-1) was a win by X?
B-2) was a win by O?
B-3) was a draw?
DID THIS IN A
'''
'''
C) Calculate the number of different possible board configurations
in all possible games (not just final boards at ends of games,
but all intermediate boards). Include the blank (beginning) board.
DID THIS IN A
'''

'''
goes through the set of boards given, and
returns a new set without transformations
'''
def without_transformation(set_boards):
    Rot90 = [6,3,0,7,4,1,8,5,2]
    Rot180 = [8,7,6,5,4,3,2,1,0]
    Rot270 = [2,5,8,1,4,7,0,3,6]
    VertFlip= [2,1,0,5,4,3,8,7,6]
    Transformations = [[Rot90],[Rot180],[Rot270],[VertFlip],[Rot90,VertFlip],[Rot180,VertFlip],[Rot270,VertFlip]]
    #now go thru each item in the list and remove
    to_return = {}
    #i think having a for i in range(len(set)) and then indexing thru
    #each after that is ok, b/c all the iterations prior to the current set we
    #are on have already been compared w this one. no point in a double comparison
    length = len(set_boards)
    list_boards = list(set_boards)
    for i in range(length):
        #make the 7 transformations of this board
        board = list_boards[i]
        print("processing board: ")
        print_board(board)
        #for j in range(i+1, length):

            #make comparisons w i's transformations and all the other elements. if
            #they're the same, don't add to to_return. if non are the same, then add to to_return
    return to_return
'''
D) Most boards in C) above are reducible to other boards.
Calculate the number of irreducible board families.
All the boards to the right are reducible to each other via
rotations of 90, 180 and 270 degrees, or a mirror flip plus a
possible added rotation by 90, 180 or 270 degrees
'''
def D(total_boards): #take the set from A
    list_of_sets = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
    for board in total_boards:
        #this is problematic b/c it's x, o and _ so they're actually all the same length
        length = 9 - board.count('_')
        list_of_sets[length - 1].add(board)
    #now that that's set up, check for transformations
    to_return = 0
    for i in range(9):
        list_of_sets[i] = without_transformation(list_of_sets[i])
        to_return += len(list_of_sets[i])

    return to_return

def main():
    a, b1, b2, b3, c, total_boards = A()
    print("A: %d \t B1: %d \t B2: %d \t B3: %d \t C: %d"%(a, b1, b2, b3, c))
    print("D: %d"%D(total_boards))

main()
