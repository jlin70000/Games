#IDLE Open Source
#Note to Viewer: Notes in code
#Jeremy Luo
#4/30


# create the game boards
user_board = [['.' for j in range(5)] for i in range(4)]
computer_board = [['.' for j in range(5)] for i in range(4)]

# Function to check if a ship already exists in the given location
def check_ship_exists(board, row, col):
    return board[row][col] == 'S'

user_guesses = [['.' for _ in range(5)] for _ in range(4)]


# Function to get a valid row and column input from user
def get_valid_input():
    while True:
        try:
            row = int(input("Please enter a row (0-3): "))
            col = int(input("Please enter a column (0-4): "))
            if row < 0 or row > 3 or col < 0 or col > 4:
                print("Invalid, try again!")
            elif check_ship_exists(user_board, row, col):
                print("Ship already exists in that location.")
            elif user_guesses[row][col] != '.':
                print("You’ve already gone here, please try again.")
            else:
                return (row, col)
        except ValueError:
            print("Invalid input. Please enter a valid integer row and column.")

# Function to print the board with headers
def print_board(board):
    print(" ", end="")
    for i in range(5):
        print(f" {i}", end="")
    print()
    print("-----")
    for row_num, row in enumerate(board):
        print(row_num, end="")
        for col in row:
            print(f" {col}", end="")
        print()

# Place 5 ships on the user board
for i in range(5):
    print(f"Placing ship {i+1}...")
    row, col = get_valid_input()
    user_board[row][col] = 'S'
    print_board(user_board)
    print("Ship placed.")

# Print the user board
print("Here is your board:")
print_board(user_board)

# Place 5 ships on the computer board
import random
for i in range(5):
    while True:
        row = random.randint(0, 3)
        col = random.randint(0, 4)
        if computer_board[row][col] == '.':
            computer_board[row][col] = 'S'
            break

# main program
turns = 0
while True:
    print("User's turn...")
    
    # get user input
    row, col = get_valid_input()
    
    # Check if the user has already guessed this location
    if user_guesses[row][col] != '.':
        print("You’ve already gone here, please try again.")
        
    # Check if the user has hit a ship
    elif computer_board[row][col] == 'S':
        print("Hit!")
        computer_board[row][col] = 'X'
        
        # Check if all ships have been sunk and print out how many turns it took
        if all('X' in row for row in computer_board):
            print("Congratulations! You win!")
            break
            if all('X' in row for row in computer_board):
                num_turns += 1
                print(f"User won in {num_turns} turns!")
                break
    # The user misses
    else:
        print("Miss!")
        computer_board[row][col] = 'O'
        turns += 1

    
    # Computer's turn
    print("Computer's turn...")
    
    # Generate random row and column for computer's guess
    while True:
        row = random.randint(0, 3)
        col = random.randint(0, 4)
        
        # Check if the computer has already guessed this location
        if user_board[row][col] == 'X' or user_board[row][col] == 'O':
            continue
            
        # Check if the computer has hit a ship
        elif user_board[row][col] == 'S':
            print("Hit!")
            user_board[row][col] = 'X'
            
            # Check if all ships have been sunk
            if all('X' in row for row in user_board):
                print("Sorry, you lose!")
                break
            
            break
        
        # the computer misses
        else:
            print("Miss!")
            user_board[row][col] = 'O'
            break
    
    # Print out the updated user board
    print_board(user_board)
    
    

