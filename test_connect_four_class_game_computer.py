'''
    CS5001 - Spring 2020
    Harshal Shah
    Project Test code for class Game_Computer
'''
import unittest
import os
from connect_the_four_classes_computer_v1 import Game_Computer
from connect_the_four_classes import Game

class Game_ComputerTest(unittest.TestCase):
    def test_init(self):
        game = Game_Computer(4, 4, "red_testing.txt", "computer_testing.txt", -100, -100)
        self.assertEqual(game.red_score, 0)
        self.assertEqual(game.computer_score, 0)
        self.assertEqual(game.rows, 4)
        self.assertEqual(game.columns, 4)
        self.assertEqual(game.board, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(game.red, 1)
        self.assertEqual(game.computer, 2)
        self.assertEqual(game.red_filename, "red_testing.txt")
        self.assertEqual(game.computer_filename, "computer_testing.txt")
        self.assertEqual(game.x, -100)
        self.assertEqual(game.y, -100)
        self.assertEqual(game.x_click, 0)
        self.assertEqual(game.y_click, 0)
        self.assertEqual(game.turn, 1)
        self.assertEqual(game.zeroes, 16)

    def test_intitalize_score(self):

        game = Game_Computer(4, 4, "red_testing.txt", "computer_testing.txt", -100, -100)
        # Initialize score from file with a non-
        # existent file; score goes back to zero
        if os.path.exists('red_testing.txt'):
            os.remove('red_testing.txt')
        if os.path.exists('computer_testing.txt'):
            os.remove('computer_testing.txt')
        game.initialize_score()
        self.assertEqual(game.red_score, 0)
        self.assertEqual(game.computer_score,0)
        
        # Initialize score from file with a score of 10
        with open('red_testing.txt', 'w') as outfile:
            outfile.write('10')
        with open('computer_testing.txt', 'w') as outfile:
            outfile.write('10')
        game.initialize_score()
        self.assertEqual(game.red_score, 10)
        self.assertEqual(game.computer_score,10)
        os.remove("red_testing.txt")
        os.remove("computer_testing.txt")
    
    

    def test_check_win_horizontal(self):
        
        game = Game_Computer(4, 4, "red_testing.txt", "computer_testing.txt", -100, -100)
        #Horizontal Winning Move
        game.board = ([0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0])
        game.check_win()
        game.initialize_score()
        #Here Red wins. So its score file should be updated from 0 to 1
        self.assertEqual(game.red_score, 1)

    def test_update_score(self):

        game = Game_Computer(4, 4, "red_testing.txt", "computer_testing.txt", -100, -100)
        if os.path.exists('red_testing.txt'):
            os.remove('red_testing.txt')
        if os.path.exists('computer_testing.txt'):
            os.remove('computer_testing.txt')
        #Update the score by one from initialized value of zero
        game.update_score(game.red)
        game.update_score(game.computer)
        
        
        #Check updated scorefiles of red and computer
        game.initialize_score()
        self.assertEqual(game.red_score, 1)
        self.assertEqual(game.computer_score,1)    
        os.remove("red_testing.txt")
        os.remove("computer_testing.txt")        
        
    def test_check_column(self):
        game = Game_Computer(3, 3, "red_testing.txt", "computer_testing.txt", -100, -100)
        
        #Zero in Row 3, Column 2 should be replaced by 1
        #Zero in Row 2, Column 2 would be replaced by 2 in computer turn
        game.check_column(game.turn)
        self.assertEqual(game.zeroes, 7)
        self.assertEqual(game.board,[[0,0,0],[0,2,0],[0,1,0]])



def main():
    
    unittest.main(verbosity = 3)
    
main()
