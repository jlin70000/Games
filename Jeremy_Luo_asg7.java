
/* Name: Jeremy Luo 
BATTLESHIP GAME
Course: [CS101]
Description: Technical notes in the program.
Date: 11/12
*/

import java.util.Scanner;

public class Jeremy_Luo_asg7 {
    final int SHIP_SIZE = 4; // constant for the size of the ship
    final int DIMENSION = 10; // constant for the size of the board 
    char[][] board = new char[DIMENSION][DIMENSION];  // create array for board
    char[][] ship = new char[DIMENSION][DIMENSION];  // 
    int score = 0; // initialize count for player's score

    // Initialize the board and randomly place the ship
    public void initializeGame() {
        // Initialize the board with empty cells
        for (int i = 0; i < DIMENSION; i++) {
            for (int j = 0; j < DIMENSION; j++) {
                board[i][j] = '.';
                ship[i][j] = '.';
            }
        }

        // Randomly place the ship
        int startRow = (int) (Math.random() * (DIMENSION - SHIP_SIZE + 1));
        int startCol = (int) (Math.random() * DIMENSION);
        boolean isVertical = Math.random() < 0.5;

        for (int i = 0; i < SHIP_SIZE; i++) {
            if (isVertical) {
            	ship[startRow + i][startCol] = 'S';
            } else {
            	ship[startRow][startCol + i] = 'S';
            }
        }
    }

    // Print the board to the console
    public void printBoard() {
        // Print column labels (A, B, C, ..., according to the board dimensions)

        System.out.print("  ");
        for (char col = 'A'; col < 'A' + DIMENSION; col++) {
            System.out.print(col + " ");
        }
        System.out.println();

        for (int i = 0; i < DIMENSION; i++) {
            // Print row number

            System.out.print((i + 1) + " ");
            // Print each cell in the row

            for (int j = 0; j < DIMENSION; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Check if a coordinate is valid (within dimension)
    public boolean isValidCoordinate(int row, int col) {
        return row >= 0 && row < DIMENSION && col >= 0 && col < DIMENSION;
    }

    // Play one turn of the game
    public void playTurn(int row, int col) {
        if (isValidCoordinate(row, col)) {
            if (ship[row][col] == 'S') { // if play equals ship, then it prints 'X' and 'HIT!'
                board[row][col] = 'X';
                System.out.println("HIT!");
                score++;
            } else if (board[row][col] != 'X') {
                board[row][col] = '#'; // if play does not equal ship, then it prints '#' and 'MISS!'
                System.out.println("MISS!");

                score++;
            }
        }
    }

    // Check if the game is won
    public boolean isGameWon() {
        for (int i = 0; i < DIMENSION; i++) {
            for (int j = 0; j < DIMENSION; j++) {
                // Check if there is a ship in this cell ('S') and it has not been hit ('X')

                if (ship[i][j] == 'S' && board[i][j] != 'X') {
                    // If a ship cell is found that has not been hit, return false

                    return false;
                }
            }
        }
        // If no ship cells that haven't been hit are found, return true (game is won)

        return true;
    }
    // MAIN PROGRAM
    public static void main(String[] args) {
        Jeremy_Luo_asg7 game = new Jeremy_Luo_asg7(); // create an instance (object) of the Jeremy_Luo_asg7 class. 
        Scanner scanner = new Scanner(System.in); // allow input

        // start game and place random ship
        game.initializeGame();
        // Continue playing until the game is won

        while (!game.isGameWon()) {
            // Display the current state of the game board

            game.printBoard();
            // prompt user to enter coordinate
            System.out.print("Enter a coordinate (e.g., B4): ");
            String input = scanner.nextLine().toUpperCase();

            // set conditions for valid input
            if (input.length() == 2 || (input.length() == 3 && input.charAt(1) == '1' && input.charAt(2) == '0')) {
                // Extract column and row information from the input

                char colChar = input.charAt(0);
                int col = colChar - 'A';
                int row;
                // Extract row information based on input length

                if (input.length() == 2) {
                    row = Character.getNumericValue(input.charAt(1)) - 1;
                } else {
                    row = 9; // For row 10
                }
                // check for duplicate play
                if (col >= 0 && col < game.DIMENSION && row >= 0 && row < game.DIMENSION) {
                    if (game.board[row][col] == 'X' || game.board[row][col] == '#') {
                        System.out.println("You have already played this spot. Please choose a different coordinate.");
                    } else {
                        game.playTurn(row, col);
                    }
                } else { // invalid inupt
                    System.out.println("Invalid input. Please enter a valid coordinate.");
                }
            } else { // invalid input
                System.out.println("Invalid input format. Please enter a valid coordinate.");
            }
        }
        // Display the final state of the game and the player's score

        System.out.println("Congratulations! You sank the ship in " + game.score + " guesses.");
        scanner.close(); // close scanner
    }
}
