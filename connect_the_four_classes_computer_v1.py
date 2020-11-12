''' CS5001 - Spring 2020
    Harshal Shah
    Project - Class Game_Computer Code
'''

import turtle
import time
import random

SQUARE_LEN = 50
CIRCLE_RADIUS = 20
TRIANGLE_SIDE = 20

class Game_Computer:
    """class: Game_Computer
       Attributes: rows, columns, red_filename, computer_filename,
                   x(x coordinate), y(y coordinate), red_score, computer_score,
                   board, red, computer, red_color, computer_color, x_click,
                   y_click, turn, zeroes
       Methods: initialize_score, update_score, draw_square, draw_circle,
                draw_triangle, display_turn, make_board, click_on_arrow,
                get_click_coordinate, check_click, check_column,
                draw_player_circle, check_win, display_winner, quit_game,
                display_score, check_draw, computer_turn, strategy_1, strategy_2                    
    """


    def __init__(self, rows, columns, red_filename,computer_filename,x , y):
        '''
           Constructor -- creates an new instance of a car
           Parameters:
           self -- the current object
           rows -- number of rows in the game board
           columns -- number of columns in the game board
           red_filename -- scorefile of the player(human) designated as red
           computer_filename -- scorefile of the computer playing the game
           x -- x coordinate of the reference point for turtle to make gameboard
           y -- y coordinate of the reference point for turtle to make gameboard
        '''

        self.red_score = 0        
        self.computer_score = 0
        
        self.rows = rows
        self.columns = columns
        #Create Game Board - Nested List
        self.board = [ [0] * self.columns for i in range(self.rows)]
        #1 & 2 represent Red & Computer positions on Game Board
        self.red = 1
        self.computer = 2
        
        self.red_filename = red_filename        
        self.computer_filename = computer_filename
        #Reference Coordinates for turtle to Create Game Board
        self.x = x
        self.y = y
        
        self.red_color = "red"       
        self.computer_color = "orange"
        self.x_click = 0
        self.y_click = 0
        #Keep Track of Turns
        self.turn = 1
        #Keep Track of unfilled positions to determine if game is a draw
        self.zeroes = self.rows * self.columns
        

    def initialize_score(self):
        '''
        Method -- initialize_score (initialize current object attribute's score to the score
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
            with open(self.computer_filename, 'r') as infile:
                self.computer_score = int(infile.read())
                
        except ValueError:
            self.computer_score = 0
        except FileNotFoundError:
            self.computer_score = 0
            

    def update_score(self, player):
        '''
        Method -- update_score (update scorefile of the winning player)
        Parameters:
           self -- the current object
           player --  human or computer
        Returns nothing
        '''

        if player == self.red:
            score = self.red_score + 1
            filename = self.red_filename
        else:
            score = self.computer_score + 1
            filename = self.computer_filename

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
            player = "Your Turn "
        
        elif self.turn % 2 == 0:
            color = "orange"
            player = "My Turn "

        turtle.clear()        
        turtle.penup()
        turtle.goto(-250,0)       
        
        turtle.color(color)
        turtle.hideturtle()
        turtle.write(player, move = False, align="center", font=("Arial", 20, "normal"))
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

        screen = turtle.Screen()
        screen.onclick(self.get_click_coordinate, 1)

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
                #Update Game Board represented by nested list by 1(player) or 2(computer)
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
        if self.turn == 2:
            self.display_turn()            
            self.computer_turn()          
            
     

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
            #Red represented by human
            color = "red"
        else:
            #Orange represented by computer
            color = "orange"

        
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
            player = self.computer

        #Check for Horizontal Winning Moves
        for i in range(self.rows):
            for j in range(self.columns - 3):
                if self.board[i][j] == player and self.board[i][j+1] == player and \
                self.board[i][j+2] == player and self.board[i][j+3] == player:                  
                    self.display_winner()
                    self.update_score(player)                   
                    self.quit_game()                                      
                    
           
        #Check Vertical Winning Moves
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
            color = "red"
            winner = "You win !!"
        else:
            color = "orange"
            winner = "I win !!"

          
        t = turtle.Turtle()
        t.penup()
        t.goto(-250,250)   
        
        t.color(color)
        
        t.write(winner , move = False, align="center", font=("Arial", 20, "normal"))
        t.hideturtle()

    def quit_game(self):
        '''
        Method -- quit_game (quit turtle screen after win or draw)        
        Parameters:
           self -- the current object
        Returns nothing
        '''

        time.sleep(1)
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
        t.goto(50,-250)        
        t.color("blue")        
        t.write("Score", move = False, align="center", font=("Arial", 20, "normal"))
        t.goto(50, -275)        
        t.write( "You: " + str(self.red_score)+ " points"
                 + "  Me: " + str(self.computer_score) + " points",
                 move = False, align="center", font=("Arial", 15, "normal"))
        t.hideturtle()

    def check_draw(self):
        '''
        Method -- check_draw(Check for draw and display on turtle screen)        
        Parameters:
           self -- the current object
        Returns nothing
        '''        
        #Count of self.zeroes is equal to rows & columns which is deducted by 1 after
        #each legal move. If it reached zero, it would indicate game is a draw
        if self.zeroes == 0:
            t = turtle.Turtle()
            t.penup()
            t.goto(-200,100)        
            t.color("blue")  
            t.write("No one wins !! Its a draw !!", move = False, align="center", font=("Arial", 15, "normal"))
            t.hideturtle()
            self.quit_game()

    def computer_turn(self):
        '''
        Method -- computer_turn(Checks for legal moves and makes move
                  which maximises chances of winning)        
        Parameters:
           self -- the current object
        Returns nothing
        '''        

        #If selected column already filled up, check next click
        time.sleep(1)
        possible_drops = []
        possible_drops_column_check = []
 
        for i in range(self.rows - 1, -1, -1):
            for j in range(self.columns):
                if len(possible_drops) == self.columns:
                    break
                #Create a list of 5 legal moves that computer can make
                if self.board[i][j] == 0 and j not in possible_drops_column_check:
                    possible_drops.append([i,j])
                    possible_drops_column_check.append(j)   

       
        #Select any 1 of the two strategy to maximise computer chances of winning
        strat_list = ["strat_1", "strat_2"]
        strat_choice = random.choice(strat_list)        
        
        if strat_choice == "strat_1":
            computer_move = self.strategy_1(possible_drops)
        elif strat_choice == "strat_2":
            computer_move = self.strategy_2(possible_drops)

        #Update Game Board Nested List
        self.board[computer_move[0]][computer_move[1]] = self.turn
        self.zeroes = self.zeroes - 1
        #Draw colored circle at selected legal move
        self.draw_player_circle(computer_move[0], computer_move[1])        
        #Check for win
        self.check_win()
        #Check for Draw
        self.check_draw()
        #Pass Turn from Computer to player
        self.turn= self.turn + 1
        if self.turn == 2:
            time.sleep(2)
            self.display_turn()
            self.computer_turn()
        if self.turn > 2:
            self.turn = 1
            self.display_turn()
            

    def strategy_1(self, possible_drops):
        '''
        Method -- strategy_1(Try to drop in columns excluding the first and last)        
        Parameters:
        self -- the current object
        possilbe_drops - list of legal moves that computer can make in its current turn
        Returns : a tuple (legal move) that computer should take
        '''
        
        boundary_drops = []   
        copy_possible_drops = possible_drops[:]
        #Include legal moves that are on first and last column
        #in boundary_drops list and rest in possible_drops
        for num in copy_possible_drops:
           
            if num[1] == 0 or num[1] == self.columns - 1:
                boundary_drops.append(num)
                possible_drops.remove(num)
        
             
        if possible_drops:
            computer_move = random.choice(possible_drops)
        else:
            computer_move = random.choice(boundary_drops)

        return computer_move
    
    def strategy_2(self, possible_drops):
        '''
        Method -- strategy_2(Out of 5 possible legal movies,
                  check spaces with most number of adjacent same color circles )        
        Parameters:
        self -- the current object
        possilbe_drops - list of legal moves that computer can make in its current turn
        Returns : a tuple (legal move) that computer should take
        '''    
        
        boundary_drops = []
        copy_possible_drops2 = possible_drops[:]
        #Include legal moves that are on boundary in boundary_drops list
        #and rest in possible_drops
        for num in copy_possible_drops2:
            if num[0] == 0 or num[0] == self.rows -1 or num[1] == 0 or num[1] == self.columns - 1:
                boundary_drops.append(num)
                possible_drops.remove(num)
       
        proximity = []
        count = 0
        if possible_drops:
            for num in possible_drops:
                #Check for number of adjacent same colored circles
                if self.board[num[0] + 1 ][num[1] + 1] == self.computer:
                    count = count + 1
                if self.board[num[0]][num[1] + 1] == self.computer:
                    count = count + 1
                if self.board[num[0] - 1 ][num[1] + 1] == self.computer:
                    count = count + 1
                if self.board[num[0] - 1 ][num[1]] == self.computer:
                    count = count + 1
                if self.board[num[0] + 1 ][num[1]] == self.computer:
                    count = count + 1
                if self.board[num[0] - 1 ][num[1] - 1] == self.computer:
                    count = count + 1
                if self.board[num[0]][num[1] - 1] == self.computer:
                    count = count + 1
                if self.board[num[0] + 1][num[1] - 1] == self.computer:
                    count = count + 1
                
                proximity.append(count)
                count = 0
            #Get the index of the max count of same colored circles adjacent to a legal move
            index = proximity.index(max(proximity))
          
            computer_move = possible_drops[index]
            
        else:
            computer_move = random.choice(boundary_drops)

        return computer_move               
     
    
