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
    #draft:
    if layout not in AllBoards.keys(): #to avoid redundant trees
        node = BoardNode(layout)
        #check if it's a winner, cuz if so obv don't add children
        winner = False
        i = 0
        while !winner and i < 8:
            if layout[wins[i][0]] != '_' and layout[wins[i][0]] == layout[wins[i][1]] and layout[wins[i][1]] == layout[wins[i][2]]:
                winner = True
            else:
                i+=1
            #now that we know which position is winning, see which character it is
        if winner:
            node.endState = layout[wins[i][0]]
        elif '_' not in layout: #means it's full. This and above are the recursive base cases
            node.endState = 'd'
        else:
            #since it's not a winner, and not full, endState is None and you can add children.
            turn = layout.count('_') #if it's odd, then it's x turn and if it's even then it's o
            if turn % 2 == 0:
                turn = 'o'
            else:
                turn = 'x'
            #now find all the places you can add x or o
            i = 0
            spots = []
            while i < 9:
                if layout[i] == '_':
                    spots.append(i)
                i+=1
            #now fill out the children, these will spawn their own CreateAllBoards calls 
            children = []
            for spot in spots:
                child = layout[:spot] + turn + layout[spot+1:]
                children.append(CreateAllBoards(child)) #remember this is valid cuz cab returns the layout
            node.children = children
        AllBoards[layout] = node
    #returns layout so that it's easy to build AllBoards
    return layout

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
