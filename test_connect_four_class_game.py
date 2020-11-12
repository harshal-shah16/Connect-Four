'''
    CS5001 - Spring 2020
    Harshal Shah
    Project Test code for class Game
'''
import unittest
import os

from connect_the_four_classes import Game

class GameTest(unittest.TestCase):
    def test_init(self):
        game = Game(4, 4, "red_testing.txt", "yellow_testing.txt", -100, -100)
        self.assertEqual(game.red_score, 0)
        self.assertEqual(game.yellow_score, 0)
        self.assertEqual(game.rows, 4)
        self.assertEqual(game.columns, 4)
        self.assertEqual(game.board, [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.assertEqual(game.red, 1)
        self.assertEqual(game.yellow, 2)
        self.assertEqual(game.red_filename, "red_testing.txt")
        self.assertEqual(game.yellow_filename, "yellow_testing.txt")
        self.assertEqual(game.x, -100)
        self.assertEqual(game.y, -100)
        self.assertEqual(game.x_click, 0)
        self.assertEqual(game.y_click, 0)
        self.assertEqual(game.turn, 1)
        self.assertEqual(game.zeroes, 16)

    def test_intitalize_score(self):

        game = Game(4, 4, "red_testing.txt", "yellow_testing.txt", -150, -150)
        # Initialize score from file with a non-
        # existent file; score goes back to zero
        if os.path.exists('red_testing.txt'):
            os.remove('red_testing.txt')
        if os.path.exists('yellow_testing.txt'):
            os.remove('yellow_testing.txt')
        game.initialize_score()
        self.assertEqual(game.red_score, 0)
        self.assertEqual(game.yellow_score,0)
        
        # Initialize score from file with a score of 10
        with open('red_testing.txt', 'w') as outfile:
            outfile.write('10')
        with open('yellow_testing.txt', 'w') as outfile:
            outfile.write('10')
        game.initialize_score()
        self.assertEqual(game.red_score, 10)
        self.assertEqual(game.yellow_score,10)
        os.remove("red_testing.txt")
        os.remove("yellow_testing.txt")
    
    

    def test_check_win_diagonal(self):
        
        game = Game(4, 4, "red_testing.txt", "yellow_testing.txt", -150, -150)
        game.turn = 2
        #Diagonal (Downward Sloping) Winning Move
        game.board = ([2,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,2])
        game.check_win()
        game.initialize_score()
        #Here Yellow wins. So its score file should be updated from 0 to 1
        self.assertEqual(game.yellow_score, 1)

    
    def test_update_score(self):

        game = Game(4, 4, "red_testing.txt", "yellow_testing.txt", -150, -150)
        if os.path.exists('red_testing.txt'):
            os.remove('red_testing.txt')
        if os.path.exists('yellow_testing.txt'):
            os.remove('yellow_testing.txt')
        #Update the score by one from initialized value of zero for both red and yellow
        game.update_score(game.red)
        game.update_score(game.yellow)
        
        
        #Check updated scorefiles of red and yellow
        game.initialize_score()
        self.assertEqual(game.red_score, 1)
        self.assertEqual(game.yellow_score,1)    
        os.remove("red_testing.txt")
        os.remove("yellow_testing.txt")        
        
    def test_check_column(self):
        game = Game(3, 3, "red_testing.txt", "yellow_testing.txt", -150, -150)        
        #Yellow Turn - And Yellow chooses third column.
        #Number of zeros on game board should be 8
        game.turn = 2
        game.check_column(2)
        self.assertEqual(game.zeroes, 8)
        self.assertEqual(game.board,[[0,0,0],[0,0,0],[0,0,2]])

        game2 = Game(3, 3, "red_testing.txt", "yellow_testing.txt", -150, -150)        
        #Red Turn - And Red chooses first column.
        #Number of zeros on game board should be 8
        game2.turn = 1
        game2.check_column(0)
        self.assertEqual(game2.zeroes, 8)
        self.assertEqual(game2.board,[[0,0,0],[0,0,0],[1,0,0]])




def main():
    
    unittest.main(verbosity = 3)
    
main()
