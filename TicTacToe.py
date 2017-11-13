#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:59:14 2017

@author: kris
"""


'''
BUG REPORT: game status at cells 4,5,6 does not return True 
'''

import sys
import os


        
def set_game():

    global c, board_cells, display_board
    c = ['1','2','3','4','5','6','7','8','9']
    board_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board = '''
         ______ ______ ______
        |  1   |  2   |  3   |
        |______|______|______|
        |  4   |  5   |  6   |
        |______|______|______|
        |  7   |  8   |  9   |
        |______|______|______|   
        '''
    start_game() 


    
def start_game():
    banner = '''
    ----------------------------------------------------
    | _____    ___   ___  ___   ___  _____  ___   ___  |
    |   |   | |       |  |   | |       |   |   | |     |
    |   |   | |       |  |---| |       |   |   | |---  |
    |   |   | |___    |  |   | |___    |   |___| |___  |
    |                                                  |
    ----------------------------------------------------
    '''
    print(banner)
    global display_board
    print('Welcome to TIC TAC TOE Game!!')
    print("Player1 your mark is 'X'.")
    print("Player2 your mark is 'Y'.")
    go = input('press ENTER to start playing!')
    if type(go) == str:
        print(display_board)
        play()
    else:
        print("Something's wrong! Run the program again.")
    
    


def print_board(mark, letter):
    global display_board
    display_board = display_board.replace(mark, letter)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_board)
       

	
    
def play():
    global board_cells
    while len(board_cells) != 0:
        while True:
            try:
                move_p1 = input('Player1, enter cell no: ')
                if board_cells.__contains__(int(move_p1)):
                    board_cells.remove(int(move_p1))
                    store_list(move_p1, 'X',)
                    print_board(move_p1, 'X')
                else:
                    print('Looks like you entered an used or invalid cell,please be careful!')
                    continue
            except ValueError:
                print('*Enter a valid number.')
                continue
            else:
                break	
        
        if game_status():
            print('Game Over!')
            again()
            break
        while True:
            try:
                move_p2 = input('Player2, enter cell no: ')            
                if board_cells.__contains__(int(move_p2)):
                    board_cells.remove(int(move_p2))
                    store_list(move_p2, 'Y',)
                    print_board(move_p2, 'Y')
                else:
                    print('Looks like you entered an used or invalid cell,please be careful!')
                    continue
            except ValueError:
                print('*Enter a valid number.')
                continue
            else:
                break
              
            
        if game_status():
            print('Game Over!')
            again()
            break
        
        
    
def store_list(x, cc):
    x = int(x)
    global c
    c[x-1] = cc 
    
    
def game_status():
    global c
    if len(board_cells) == 0:
        print('No more cells.This match is a Draw!')
        return True
    if (c[0] == c[1] == c[2]) or (c[0] == c[4] == c[8]) or (c[0] == c[3] == c[6]) or (c[1] == c[4] == c[7]) or (c[2] == c[5] == c[8]) or (c[6] == c[7] == c[8]) or (c[2] == c[4] == c[6]):
        if ((c[0] == c[1] == c[2]) and c[0]=='X') or ((c[0] == c[4] == c[8]) and c[0]=='X') or ((c[0] == c[3] == c[6]) and c[0]=='X') or ((c[1] == c[4] == c[7])and c[1]=='X') or ((c[2] == c[5] == c[8])and c[2]=='X') or ((c[6] == c[7] == c[8]) and c[6]=='X') or ((c[2] == c[4] == c[6]) and c[2]=='X') or ((c[3] == c[4] == c[5]) and c[4]=='X'):
            print('Congratulations player one, You are the winner!')
            return True
        elif ((c[0] == c[1] == c[2]) and c[0]=='Y') or ((c[0] == c[4] == c[8]) and c[0]=='Y') or ((c[0] == c[3] == c[6]) and c[0]=='Y') or ((c[1] == c[4] == c[7]) and c[1]=='Y') or ((c[2] == c[5] == c[8]) and c[2]=='Y') or ((c[6] == c[7] == c[8]) and c[6]=='Y') or ((c[2] == c[4] == c[6]) and c[2]=='Y') or ((c[3] == c[4] == c[5]) and c[4]=='Y'):
            print('Congratulations player two, You are the winner!')
            return True
        return True           
    else:
        return False
        
              
def again():
    string_a = input('Do you want to play again: ').lower()
    if string_a.startswith('y') or string_a == '':
        set_game()    
    elif string_a.startswith('n'):
        print('Thanks for playing!! Hope you had lots of fun!')
        sys.exit()
    else:
        print("Taken that as a 'no', Thanks for playing!")
        sys.exit() 

set_game()        
