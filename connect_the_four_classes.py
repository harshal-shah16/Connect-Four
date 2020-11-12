''' CS5001 - Spring 2020
    Harshal Shah
    Project - Class Game Code
'''

import turtle
import time

SQUARE_LEN = 50
CIRCLE_RADIUS = 20
TRIANGLE_SIDE = 20

class Game:
    """class: Game
       Attributes: rows, columns, red_filename, yellow_filename,
                   x(x coordinate), y(y coordinate), red_score, yellow_score,
                   board, red, yellow, red_color, yellow_color, x_click,
                   y_click, turn, zeroes
       Methods: initialize_score, update_score, draw_square, draw_circle,
                draw_triangle, display_turn, make_board, click_on_arrow,
                get_click_coordinate, check_click, check_column,
                draw_player_circle, check_win, display_winner, quit_game,
                display_score, check_draw                    
    """


    def __init__(self, rows, columns, red_filename,yellow_filename, x, y):

        self.red_score = 0
        self.yellow_score = 0
        self.rows = rows
        self.columns = columns
        #Create Game Board - Nested List
        self.board = [ [0] * self.columns for i in range(self.rows)]
        #1 & 2 represent Red & Yellow positions on Game Board
        self.red = 1
        self.yellow = 2
        self.red_filename = red_filename
        self.yellow_filename = yellow_filename
        #Reference Coordinates for turtle to Create Game Board
        self.x = x
        self.y = y
        self.red_color = "red"
        self.yellow_color = "yellow"
        self.x_click = 0
        self.y_click = 0
        #Keep Track of Turns
        self.turn = 1
        #Keep Track of unfilled positions to determine if game is a draw
        self.zeroes = self.rows * self.columns        
      

    def initialize_score(self):
        '''
        Method -- initialize_score (initialize current object's score to the score
                  in the score text file)
        Parameters:
           self -- the current object           
        Returns nothing
        '''
        
        try:
            with open(self.red_filename, 'r') as infile:
                self.red_score = int(infile.read())
                
        except ValueError:
            self.red_score = 0
        except FileNotFoundError:
            self.red_score = 0

        try:
            with open(self.yellow_filename, 'r') as infile:
                self.yellow_score = int(infile.read())
                
        except ValueError:
            self.yellow_score = 0
        except FileNotFoundError:
            self.yellow_score = 0
            

    def update_score(self, player):
        '''
        Method -- update_score (update scorefile of the winning player)
        Parameters:
           self -- the current object
           player --  Red player or Yellow Player
        Returns nothing
        '''

        if player == self.red:
            score = self.red_score + 1
            filename = self.red_filename
        else:
            score = self.yellow_score + 1
            filename = self.yellow_filename

        try:
            with open(filename, "w") as outfile:
                outfile.write(str(score))
        
        except OSError:
                print("Could not update your file")    
            
    

    def draw_square(self, x, y):
        '''
        Method -- draw_square (draws square at given x & y coordinate)
        Parameters:
           self -- the current object
           x --  x coordinate at which turtle will start drawing square
           y --  y coordinate at which turtle will start drawing square
        Returns nothing
        '''

        turtle.tracer(10,0)
        t = turtle.Turtle()
        t.penup()
        t.setpos(x, y)
        t.fillcolor("blue")
        t.begin_fill()
        t.forward(SQUARE_LEN)
        t.right(90)
        t.forward(SQUARE_LEN)
        t.right(90)
        t.forward(SQUARE_LEN)
        t.right(90)
        t.forward(SQUARE_LEN)
        t.right(90)
        t.end_fill()
        t.hideturtle()
        turtle.tracer(10,0)

    def draw_circle(self, x, y):
        '''
        Method -- draw_circle (draws circle at given x & y coordinate)
        Parameters:
           self -- the current object
           x --  x coordinate at which turtle will start drawing circle
           y --  y coordinate at which turtle will start drawing circle
        Returns nothing
        '''

        t = turtle.Turtle()
        t.penup()
        t.setpos(x, y)
        t.fillcolor("white")
        t.begin_fill()
        t.circle(CIRCLE_RADIUS)
        t.end_fill()
        t.hideturtle()
        turtle.tracer(10,0)

    def draw_triangle(self, x,y):
        '''
        Method -- draw_triangle (draws triangle at given x & y coordinate)
        Parameters:
           self -- the current object
           x --  x coordinate at which turtle will start drawing triangle
           y --  y coordinate at which turtle will start drawing triangle
        Returns nothing
        '''

        t = turtle.Turtle()
        t.penup()
        t.setpos(x, y)
        t.fillcolor("black")
        t.begin_fill()
        t.forward(TRIANGLE_SIDE)
        t.right(120)
        t.forward(TRIANGLE_SIDE)
        t.right(120)
        t.forward(TRIANGLE_SIDE)
        t.right(120)
        t.end_fill()
        t.hideturtle()
        turtle.tracer(10,0)

    def display_turn(self):
        '''
        Method -- draw_triangle (draws triangle at given x & y coordinate)
        Parameters:
           self -- the current object
           x --  x coordinate at which turtle will start drawing triangle
           y --  y coordinate at which turtle will start drawing triangle
        Returns nothing
        '''

        if self.turn % 2 == 1:
            color = "red"
        else:
            color = "yellow"

        turtle.clear()        
        turtle.penup()
        turtle.goto(-250,0)       
        
        turtle.color(color)
        turtle.hideturtle()
        turtle.write(str.upper(color) + " Turn", move = False, align="center", font=("Arial", 20, "normal"))
        turtle.setpos(-300, 50)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.hideturtle()


    def make_board(self):
        '''
        Method -- make_board (turtle creates game board)
        Parameters:
           self -- the current object
        Returns nothing
        '''

        xcor = self.x
        ycor = self.y
        #Draw Game Board Squares
        for i in range(self.rows):
            for j in range(self.columns):
                self.draw_square(xcor, ycor)
                xcor = xcor + SQUARE_LEN
            xcor = self.x
            ycor = ycor + SQUARE_LEN

        xcor_circle = self.x + 25
        ycor_circle = self.y + -45

        #Draw Circles in each square of Game Board
        for i in range(self.rows):
            for j in range(self.columns):
                self.draw_circle(xcor_circle, ycor_circle)
                xcor_circle = xcor_circle + SQUARE_LEN
            xcor_circle = self.x + 25
            ycor_circle = ycor_circle + SQUARE_LEN

        xtri = self.x + 15
        ytri = self.y + self.rows * SQUARE_LEN - 20

        #Draw Triangles (To Select Column for the move)
        for i in range(self.columns):
            self.draw_triangle(xtri, ytri)
            xtri = xtri + SQUARE_LEN

    def click_on_arrow(self):
        '''
        Method -- click_on_arrow (listen to mouse click)
        Parameters:
           self -- the current object
        Returns nothing
        '''

        s = turtle.Screen()
        s.onclick(self.get_click_coordinate, 1)

    def get_click_coordinate(self, x_click, y_click):
        '''
        Method -- get_click_coordinate (capture x & y coordinates of mouse click)
        Parameters:
           self -- the current object
           x -- x coordinate of mouse click
           y -- y coordinate of mouse click
        Returns nothing
        '''
        
        self.x_click = x_click
        self.y_click = y_click
        self.check_click()

    def check_click(self):
        '''
        Method -- check_click (check if the click has been clicked on triangles
                               representing the game board columns)
        Parameters:
           self -- the current object
           x -- x coordinate of mouse click
           y -- y coordinate of mouse click
        Returns nothing
        '''
     
        #To check if the coordinate of the mouseclick overlap with any of the
        #triangles representing game board columns beneath them
        
        for i in range(0, self.columns * SQUARE_LEN - 20, SQUARE_LEN):
            
            if self.x_click > self.x + 15 + i and self.x_click < self.x + 35 + i \
            and self.y_click < self.x + (self.rows - 1) * SQUARE_LEN + 30 \
            and self.y_click > self.x + (self.rows - 1) * SQUARE_LEN + 10:
                self.check_column(i // SQUARE_LEN)
                

    def check_column(self, selected_column):
        '''
        Method -- check_column (check if selected column is legal move
                                and update game board)
        Parameters:
           self -- the current object
           x -- x coordinate of mouse click
           y -- y coordinate of mouse click
        Returns nothing
        '''
        #If selected column already filled up, do not pass turn to computer and check
        #for current player's new click's validity
        sublist = []
        for i in range(self.rows):
            sublist.append(self.board[self.rows - i - 1][selected_column])

        if 0 not in sublist:
            self.click_on_arrow()            
            return  
                
            
        for i in range(self.rows):
            
            if self.board[self.rows - i - 1][selected_column] == 0:
                #Update Game Board represented by nested list by Player 1 or Player 2
                self.board[self.rows - i -1][selected_column] = self.turn
                #Deduct the number of zeroes by 1. Declare the game a draw if count of zeroes reach 0
                self.zeroes = self.zeroes - 1
                #Draw circle on the legal move selected by the player
                self.draw_player_circle(self.rows - i - 1, selected_column)
                break     
        #Check for a draw
        self.check_draw()
        #Check for a win
        self.check_win()
        #Pass the turn to computer
        self.turn= self.turn + 1
        if self.turn > 2:
            self.turn = 1
        self.display_turn()
        

    def draw_player_circle(self, selected_row, selected_column):
        '''
        Method -- draw_player_circle (draw circle at player's selected legal move)
        
        Parameters:
           self -- the current object
           selected_row -- row in which the circle is to be drawn and colored
           selected_column -- column in which the circle is to be drawn and colored
        Returns nothing
        '''


        xcor_circle = self.x + (SQUARE_LEN / 2)
        ycor_circle = self.y + -(SQUARE_LEN / 2 + CIRCLE_RADIUS)

        if self.turn % 2 == 1:
            color = "red"
        else:
            color = "yellow"

        t = turtle.Turtle()
        t.penup()
        t.setpos(xcor_circle + selected_column * SQUARE_LEN, ycor_circle + (self.rows - selected_row - 1) * SQUARE_LEN)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(CIRCLE_RADIUS)
        t.end_fill()
        t.hideturtle()
        turtle.tracer(10,0)       
        
            
    def check_win(self):
        '''
        Method -- check_win (check if the current game board positions represent a win
                            for current player)        
        Parameters:
           self -- the current object
        Returns nothing
        '''

        if self.turn % 2 == 1:
            player = self.red
        else:
            player = self.yellow

        #Check for Horizontal Winning Moves
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.board[i][j] == player and self.board[i][j+1] == player and \
                self.board[i][j+2] == player and self.board[i][j+3] == player:               
                    self.display_winner()
                    self.update_score(player)                   
                    self.quit_game()                    
                    
           
        #Check for Vertical Winning Moves
        for i in range(self.rows - 3):
            for j in range(self.columns):
                if self.board[i][j] == player and self.board[i+1][j] == player  and \
                self.board[i+2][j] == player and self.board[i+3][j] == player:
                    self.display_winner()
                    self.update_score(player)
                    self.quit_game()               
                    
                    
        #Check for Diagonal(Downward Sloping) Winnning Moves
        for i in range(self.rows - 3):
            for j in range(self.columns - 3):
                if self.board[i][j] == player and self.board[i+1][j+1] == player \
                and self.board[i+2][j+2] == player and self.board[i+3][j+3] == player:
                    self.display_winner()
                    self.update_score(player)
                    self.quit_game()
                    

        #Check for Diagonal(Upward Sloping) Winning Moves
        for i in range(self.rows - 1, 2, - 1):
            for j in range(self.columns - 3):
                if self.board[i][j] == player and self.board[i-1][j+1] == player \
                and self.board[i-2][j+2] == player and self.board[i-3][j+3] == player:
                    self.display_winner()
                    self.update_score(player)
                    self.quit_game()
     
                    
    def display_winner(self):
        '''
        Method -- display_winner (display winnning message on turtle screen)        
        Parameters:
           self -- the current object
        Returns nothing
        '''
        
        if self.turn % 2 == 1:
            winner = "RED"
        else:
            winner = "YELLOW"

          
        t = turtle.Turtle()
        t.penup()
        t.goto(-250,250) 
        
        t.color(str.lower(winner))        
        
        t.write(winner + " wins !!", move = False, align="center", font=("Arial", 20, "normal"))
        t.hideturtle()

    def quit_game(self):
        '''
        Method -- quit_game (quit turtle screen after win or draw)        
        Parameters:
           self -- the current object
        Returns nothing
        '''

        time.sleep(2)
        turtle.bye()

    def display_score(self):
        '''
        Method -- display_score (Display scores accumulated so far on turtle screen)        
        Parameters:
           self -- the current object
        Returns nothing
        '''

        t = turtle.Turtle()
        t.penup()
        t.goto(50,-225)        
        t.color("blue")        
        t.write("Score", move = False, align="center", font=("Arial", 20, "normal"))
        t.goto(50, -250)        
        t.write( "Red: " + str(self.red_score)+ " points"
                 + "  Yellow: " + str(self.yellow_score) + " points",
                 move = False, align="center", font=("Arial", 15, "normal"))
        t.hideturtle()

    def check_draw(self):
        '''
        Method -- check_draw(Check for draw and display on turtle screen)        
        Parameters:
           self -- the current object
        Returns nothing
        '''       

        if self.zeroes == 0:
            t = turtle.Turtle()
            t.penup()
            t.goto(-250,100)        
            t.color("blue")  
            t.write("No one wins !! Its a draw !!", move = False, align="center", font=("Arial", 15, "normal"))
            t.hideturtle()
            self.quit_game()           
                

    
