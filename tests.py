import unittest
import os
from subprocess import Popen, PIPE, STDOUT

from tic_tac_toe_adv import TicTacToe

class BoardCheck(unittest.TestCase):

    def test_good_size(self):
        """Test to check if the board accepts sizes 3 to 5 inclusive
        """
        for size in range(3, 6):
            tic = TicTacToe()
            tic._create_board(size = size)
            expected_output = [["_" for _ in range(size)] for _ in range(size)]
            self.assertEqual(tic.board, expected_output)


    def test_bad_size(self):
        """Test to check if the board dismisses sizes out of range
        """
        bad_sizes = (1, 2, 6)
        for size in bad_sizes:
            tic = TicTacToe()
            tic._create_board(size = size)
            self.assertEqual(tic.board, [])   

class NameCheck(unittest.TestCase):

    def test_name(self):
        f = open(os.devnull, 'w')
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE, stderr = f)
        out = p.communicate(input = "John\nNash".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertTrue("Player 1 is John" in out and "Player 2 is Nash" in out)
        f.close()

    def test_same(self):
        f = open(os.devnull, 'w')
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE, stderr = f)
        out = p.communicate(input = "John\nJohn".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertFalse("Player 1 is John" in out and "Player 2 is John" in out)
        f.close()

class WinCheck(unittest.TestCase):

    def test_win_function(self):
        """Test to check correctness of the win function
        """
        tic = TicTacToe()
        
        # for row
        tic.board = [
            ["_", "_", "X"],
            ["X", "O", "X"],
            ["O", "O", "O"]
        ]

        win = tic._check_player_win("O")
        self.assertTrue(win)

        # for column
        tic.board = [
            ["X", "_", "X", "_"],
            ["X", "_", "O", "_"],
            ["X", "O", "O", "_"],
            ["X", "O", "O", "_"]
        ]

        win = tic._check_player_win("X")
        self.assertTrue(win)

        # for diagonal
        tic.board = [
            ["X", "_", "X", "X", "O"],
            ["O", "X", "O", "X", "O"],
            ["X", "O", "X", "_", "O"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "O", "X", "X"]
        ]

        win = tic._check_player_win("X")
        self.assertTrue(win)

    def test_simulate(self):
        """Test to play a game resulting in a win
        """
        # first player wins
        print("Testing Simulation for a first player win")
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE)
        out = p.communicate(input = "John\nNash\n3\n1 1\n1 2\n2 2\n3 2\n3 3".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertTrue("wins the game!" in out)

        # second player wins
        print("Testing Simulation for a second player win")
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE)
        out = p.communicate(input = "John\nNash\n3\n1 1\n1 3\n2 1\n3 1\n3 3\n2 2".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertTrue("wins the game!" in out)

class DrawCheck(unittest.TestCase):

    def test_draw_function(self):
        """Test to check correctness of the draw function
        """
        tic = TicTacToe()
        
        # for row
        tic.board = [
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["X", "O", "X"]
        ]

        win = tic._check_player_win("O")
        self.assertFalse(win)
        self.assertTrue(tic._check_board_filled())

        # for column
        tic.board = [
            ["X", "X", "X", "O"],
            ["X", "X", "O", "X"],
            ["X", "O", "O", "O"],
            ["O", "O", "O", "X"]
        ]

        win = tic._check_player_win("X")
        self.assertFalse(win)
        self.assertTrue(tic._check_board_filled)

        # for diagonal
        tic.board = [
            ["X", "X", "X", "X", "O"],
            ["O", "O", "O", "X", "O"],
            ["X", "X", "X", "O", "O"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "O", "X", "X"]
        ]

        win = tic._check_player_win("X")
        self.assertFalse(win)
        self.assertTrue(tic._check_board_filled)

    def test_simulate(self):
        """Test to play a game resulting in a draw
        """
        print("Testing Simulation for a drawn match")
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE)
        out = p.communicate(input = "John\nNash\n3\n1 1\n2 2\n1 2\n3 2\n3 1\n2 1\n2 3\n1 3\n3 3".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertFalse("wins the game!" in out)
        self.assertTrue("Match Draw!" in out)

class ErrorCheck(unittest.TestCase):

    def test_invalid_coordinate(self):
        """Test to check if invalid coordinates like (3a, 1, abc s) and out of range coordinates are caught
        """
        print("Testing Error Cases")
        f = open(os.devnull, 'w')
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE, stderr = f)
        out = p.communicate(input = "John\nNash\n3\n11\nabc\n4 4\n".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertTrue(out.count("Please enter valid coordinates") == 3)
        f.close()

    def test_busy_coordinates(self):
        """Test to check if already marked coordinates are caught
        """
        print("Testing Error Cases")
        f = open(os.devnull, 'w')
        p = Popen(["python", "tic_tac_toe_adv.py"], stdin = PIPE, stdout = PIPE, stderr = f)
        out = p.communicate(input = "John\nNash\n3\n1 1\n1 1\n".encode())[0]
        out = out.decode()
        print(out, "\n")
        self.assertTrue("Incorrect move" in out)
        f.close()


if __name__ == '__main__':
    unittest.main() 
