# AI_Checkers
AI Checkers Using State Space Search

Project coded by Bryce Yahn
CSC 242
Due Sept 24 2019

1) How to build your project
This is Python so there is no need to build it.

2) How to run your project's programs

To run, enter the Checkers folder and run
$ python3 MainGame.py

The MainGame file includes a main method which will set up the rest of
the game. The program uses user input to determine the board size, which player is black and white, and the depth of the
H-minimax cutoff function if the game is played on an 8x8 board.

The Initialize file sets up the initial state, and gets user input for the board size, color, and depth of the H-minimax
cutoff function.  It sets up the board based on the board size and establishes the initial state of the game.

The State class is defined by a board and a current player.  This is the game state.  This class also has the
applicability function get_possible_actions() which makes a queue of states that are the results of the possible
actions. It also has the function check_terminal_state() which checks if the current state is the terminal state and
get_utility() which returns the utility of the terminal state.

The file MoveMaker contains the functions necessary for game play.  This includes the method play() which runs one turn
(either the computer's or the person's).  This file also contains minimax(), h-minimax(), cutoff(), and eval() which is
the heuristic function.  The heuristic involves a weighted difference of the computers pieces and the person's pieces.
This file also contains methods for parsing user input and determining the legality of the person's move.

The MainGame file runs the initialization of the game, then plays the game until someone wins or there's a tie.
Then it asks if the person wants to play again, and if they do, it will repeat the process.  Otherwise, it ends.

