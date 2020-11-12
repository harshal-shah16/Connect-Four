''' CS5001 - Spring 2020
    Harshal Shah
    Project - Driver File
'''

from connect_four_non_class_functions import game_mode
from connect_four_non_class_functions import choose_board_size
from connect_the_four_classes_computer_v1 import *
from connect_the_four_classes import *

def main():
    
    #Get User Choice (Human vs Human or Human vs Computer)
    choice = game_mode()
    #Get User Choice (GameBoard Dimensions)
    (rows, columns) = choose_board_size()

    if choice == 1:
        #Human vs Human
        game = Game(rows, columns, "red.txt", "yellow.txt", -100, -100)
        game.make_board()
        game.initialize_score()
        game.display_score()
        game.display_turn()
        game.click_on_arrow()
    else:
        #Human vs Computer
        game = Game_Computer(rows, columns, "red.txt", "computer.txt", -100, -100)
        game.make_board()
        game.initialize_score()
        game.display_score()
        game.display_turn()
        game.click_on_arrow()

main()




