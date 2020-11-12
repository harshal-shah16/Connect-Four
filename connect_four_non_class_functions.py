"""
    CS5001
    Harshal Shah - Spring 2020
    Project - Non-Class Functions Code
    
"""


def game_mode():
    """ Function: game_mode
        Parameter: No parameters
        Does: Prints game menu and gets user choice
        Returns: Choice of Game Mode selected by User
    """

    print("***********************")
    print("Welcome to Connect Four")
    print("***********************")
    print("Before we start Select from following options\n")
    print("Enter 1 for Human versus Human mode\n")
    print("Enter 2 for Human versus Computer mode\n")
    
    #Default choice to Human versus Human mode if ValueError is raised
    try:
        choice = int(input("Enter your choice\n"))
    except ValueError:
        print("Human Verus Human Game Mode\n")
        return 1
    while choice != 1 and choice != 2:
        choice = int(input(("Invalid Choice. Please Enter 1 or 2\n")))
    return choice

def choose_board_size():
    """Function: choose_board_size
        Parameter: No parameters
        Does: Gets rows and columsn for game
        Returns: Choice of Game Mode selected by User
    """
     
    answer = input("Do you want to select default size for the game ? Enter Yes or No \n")
    
    if str.upper(answer) == "YES" or str.upper(answer) == "Y":
        print("Great !! Let's Play !!\n")
        return (6,7)

    else:    
        print("\nLet's select Connect Four Game Board Size !\n")
        #Default rows 6 if ValueError is raised
        try:
            rows = int(input("Please enter number of rows for your board. Should be atleast 4 and less than 11\n"))
        except ValueError:
            rows = 6
        while rows < 4 or rows > 10:
            rows = int(input(("Invalid Choice. Please Enter a number between 4 and 10\n")))
            
        #Default Columns to 7 if ValueError is raised
        try:
            columns = int(input("Please enter number of columns for your board. Should be atleast 4 and less than 11\n"))
        except ValueError:
            columns = 7
        while columns < 4 or columns > 10:
            columns = int(input(("Invalid Choice. Please Enter a number between 4 and 10\n")))

        print("Great !! Let's Play !!\n")

        return (rows, columns)




    
