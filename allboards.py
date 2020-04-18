#! /usr/bin/python3

import sys
import time
import copy

''' Layout positions:
0 1 2
3 4 5
6 7 8

layouts look like "_x_ox__o_"

'''

#globals -- thanks mssr. Brooks
Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode



class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('children:',self.children)

#I took out the parent param cuz I found it unecessary -- the num of _ should work the same
def CreateAllBoards(layout):
    global wins, AllBoards
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    return 0

'''
* print out # of boards in AllBoards
* print # of children for all BoardNodes in AllBoards (should be high #)
* print # of boards that are xwins, then that are owins, then that are draws,
  then that are neither (should add to # of boards)
*
'''
def main():
    global AllBoards
    CreateAllBoards("_________")
    print("Number of elements in AllBoards: ")
    print(len(AllBoards))
    #get all the info
    xwins = 0
    owins = 0
    draw = 0
    not_win = 0
    total_children = 0
    for board in AllBoards:
        state = AllBoards[board].endState
        if state is None:
            not_win += 1 #i put this first to avoid nonetype error
        elif state == 'x':
            xwins+=1
        elif state == 'o':
            owins+=1
        elif state == 'd':
            dwins+=1
        num_children = len(AllBoards[board].children)
        total_children+=num_children
    print("xwins: %d\t owins: %d\t draws: %d\t not_win: %d\t totalkids: %d\t"%(xwins, owins, draws, not_win, total_children))
    return 0
