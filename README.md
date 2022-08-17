## Tic Tac Toe

### Basic Tutorial  
The game is located in the python file ```tic_tac_toe_adv.py``` and supports Python 3.5+ atleast. To run the game:
```bash
python tic_tac_toe_adv.py
```
*Note*: Make sure that the version of python is correct, if needed use ```python3``` instead of ```python```.  
Running the above command will pop up prompts for the players to enter their names. The names need to be distinct for the game to move forward.  
```bash
Waiting for the players to join...
Enter first player name : 
```
Following this, the user would be prompted to input a board size between 3 and 5 inclusive. A value out of range or non-numeric will cause the game to exit. 
```bash
lets start the Game!!

Please choose the board grid, choose one among them  !!


Enter board size between 3 and 5:
```
After a value is chosen, an empty board will pop up on the screen prompting a random player amongst the two to start the game.  
```
Player John turn
_ _ _
_ _ _
_ _ _
Enter row and column numbers to fix spot:
```
The prompt asks for the coordinates of the position that the player wants to mark (with an X or O). The proper format of the coordinates is ```<row> <column``` for example ```1 1``` and ```3 3``` as the extremes of the ```3x3``` board. Improper coordinates (non-numeric strings) or coordinates out of range will be ignored and the player would be asked to re-enter the coordinates.  
```
Player Nash turn
X _ X
_ O _
_ _ _
Enter row and column numbers to fix spot: 1 2
```
Subsequent turns will continue to fill the board until a player wins by normal Tic Tac Toe rules or the board completely fills up, in which case, it is a draw. An example of a win and a draw are shown.
```
Player John wins the game!

X X X
_ O O
_ _ _
``` 
```
Match Draw!

O X O
O X X
X O O
```

### Running Tests
To run the tests, just use the following command after ensuring that the test file (```tests.py```) is in the same directory as the game file (```tic_tac_toe_adv.py```)
```bash
python tests.py
```
Upon a successful run, the following would be printed on the terminal to the user know.
```
----------------------------------------------------------------------
Ran 10 tests in 0.746s

OK
```