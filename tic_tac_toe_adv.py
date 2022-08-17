import random
import os

# os.system("cls")

class TicTacToe:
    def __init__(self):
        self.board = []

    def _create_board(self, size):
        """Creates a squared board with size as input from user
        """
        if size <= 5 and size >= 3:
            for _ in range(size):
                row = []
                for _ in range(size):
                    row.append("_")
                self.board.append(row)
        else:
            print("Board size should be in 3 to 5")

    def _random_starting_player(self):
        """Randomly chooses a starting player
        """
        return random.choice(("X", "O"))

    def _coordiante_spot(self, row, col, player):
        """Marks a space on the board depending on the coordinate and the player
        """
        self.board[row][col] = player

    def _check_player_win(self, player):
        """Checks if the corresponding player has won
        """
        win = False
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win: return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win: return win

        # checking main diagonal
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win: return win

        # checking other diagonal
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        return win

    def _check_board_filled(self):
        """Checks if the board has no empty space left
        """
        marks = [item for row in self.board for item in row]
        return "_" not in marks

    def _change_player_turn(self, player):
        """Alternates between Player 1 and Player 2
        """
        return "X" if player == "O" else "O"

    def show_board(self):
        """Prints board on the terminal
        """
        for row in self.board:
            for item in row:
                print(item, end = " ")
            print()

    def start(self):
        """Start the game sequence
        """

        # Asking for the player names and if the names are the same it will ask again.
        print("Waiting for the players to join...")
        player1 = input("Enter first player name : ")
        print(f"Player 1 is {player1}")
        print("Waiting for the 2nd player to join...")
        player2 = input("Enter second player name : ")
        
        # player names need to be distinct
        while player1 == player2:
            print("Players cannot be same")
            player2 = input("Enter second player name : ")
        print("Player 2 is " + player2 )
        self.player_names = {
            "X": player1,
            "O": player2
        }

        # Asking the user to choose the board size.
        print("lets start the Game!! \n")
        print("Please choose the board grid, choose one among them  !! \n \n")

        # create board and start the game
        size = int(input("Enter board size between 3 and 5: "))
        self._create_board(size)
        if not self.board: exit()

        player = self._random_starting_player()
        while True:
            print(f"Player {self.player_names[player]} turn")
            self.show_board()
            valid_input = False

            # taking user input
            while True:
                try:
                    row_temp, col_temp = list(map(int, input("Enter row and column numbers to fix spot: ").split()))

                    if self.board[row_temp - 1][col_temp - 1] == "X" or self.board[row_temp - 1][col_temp - 1] == "O":
                        print("Incorrect move, please choose another spot")
                    else:
                        row = row_temp
                        col = col_temp
                        valid_input = True

                    print()
                    break
                except ValueError:
                    print("Please enter valid coordinates separated by *space* e.g. ...  1 1")
                except IndexError:
                    print("Please enter valid coordinates, should be within the board i.e. <= {}". format(len(self.board)))
            
            if not valid_input:
                continue

            # fixing the spot
            self._coordiante_spot(row - 1, col - 1, player)

            # check if the current player has won or not
            if self._check_player_win(player):
                print(f"Player {self.player_names[player]} wins the game!")
                break

            # check whether the game is draw or not
            if self._check_board_filled():
                print("Match Draw!")
                break

            # swap turn
            player = self._change_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


if __name__ == "__main__":
    # starting the game
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()