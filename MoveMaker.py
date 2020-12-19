from State import State
import random


class MoveMaker:

    def __init__(self, game_size, curr_state, computer, max_depth):
        self.game_size = game_size
        self.curr_state = curr_state
        self.computer = computer
        self.max_depth = max_depth
        self.instructions = "One player can move only white pieces.  The other player can move only black pieces.\n" \
                       "The board starts with black pawns ('b') and white pawns ('w').\n\n" \
                       "Pawns can either move forward 1 step into a blank space or hop forward over an opponents piece, capturing it.\n" \
                       "If a capture can be made, you must make that capture.  Furthermore, you can make multiple captures in one move.\n" \
                       "You must make the longest series of captures possible on the board at a given time.\n\n" \
                       "If a pawn reaches the other side of the board, it becomes a king.  Kings can move forward or backwards.\n" \
                       "White kings are represented by a 'W' and black kings are represented by a 'B'\n\n" \
                       "The object of the game is to take all of the opponent's pieces.  A player loses when they can no longer make any moves.\n" \
                       "In our game, I will print the board after each move so you can see where the pieces are.\n\n" \
                       "In order to move a piece, enter the starting square of the piece and the landing square of the piece separated by a dash '-' such as:\n" \
                       "A2 - B3  or  D3 - C2   Each element in your input must be separated by spaces.\n\n" \
                       "In order to make a capture, again enter the starting square and the landing square of the piece you would like to move, but this time separate them by an 'X' such as\n" \
                       "A2 X C4  or  D3 X B1  .\n\nIn order to make multiple captures, enter each of the landing squares with X's in between, such as \n" \
                       "A2 X C4 X E6\n\n"
        print("\n\nOkay!  Here are the instructions.  You can refer back to these at any time on your turn by entering "
              "'?' instead of a move\n")
        print(self.instructions)
        print('Alright! I think that is everything. Let the game begin!\n\n\n')
        self.curr_state.print_board()
        if self.computer == 1:
            print('Looks like it is my turn!\n')
        # The corresponding board name and locations
        if self.game_size == 4:
            self.board_names = {
                'A2': (0, 1),
                'A4': (0, 3),
                'A6': (0, 5),
                'A8': (0, 7),
                'B1': (1, 0),
                'B3': (1, 2),
                'B5': (1, 4),
                'B7': (1, 6),
                'C2': (2, 1),
                'C4': (2, 3),
                'C6': (2, 5),
                'C8': (2, 7),
                'D1': (3, 0),
                'D3': (3, 2),
                'D5': (3, 4),
                'D7': (3, 6),
                'a2': (0, 1),
                'a4': (0, 3),
                'a6': (0, 5),
                'a8': (0, 7),
                'b1': (1, 0),
                'b3': (1, 2),
                'b5': (1, 4),
                'b7': (1, 6),
                'c2': (2, 1),
                'c4': (2, 3),
                'c6': (2, 5),
                'c8': (2, 7),
                'd1': (3, 0),
                'd3': (3, 2),
                'd5': (3, 4),
                'd7': (3, 6),
            }
        else:
            self.board_names = {
                'A2': (0, 1),
                'A4': (0, 3),
                'A6': (0, 5),
                'A8': (0, 7),
                'B1': (1, 0),
                'B3': (1, 2),
                'B5': (1, 4),
                'B7': (1, 6),
                'C2': (2, 1),
                'C4': (2, 3),
                'C6': (2, 5),
                'C8': (2, 7),
                'D1': (3, 0),
                'D3': (3, 2),
                'D5': (3, 4),
                'D7': (3, 6),
                'E2': (4, 1),
                'E4': (4, 3),
                'E6': (4, 5),
                'E8': (4, 7),
                'F1': (5, 0),
                'F3': (5, 2),
                'F5': (5, 4),
                'F7': (5, 6),
                'G2': (6, 1),
                'G4': (6, 3),
                'G6': (6, 5),
                'G8': (6, 7),
                'H1': (7, 0),
                'H3': (7, 2),
                'H5': (7, 4),
                'H7': (7, 6),
                'a2': (0, 1),
                'a4': (0, 3),
                'a6': (0, 5),
                'a8': (0, 7),
                'b1': (1, 0),
                'b3': (1, 2),
                'b5': (1, 4),
                'b7': (1, 6),
                'c2': (2, 1),
                'c4': (2, 3),
                'c6': (2, 5),
                'c8': (2, 7),
                'd1': (3, 0),
                'd3': (3, 2),
                'd5': (3, 4),
                'd7': (3, 6),
                'e2': (4, 1),
                'e4': (4, 3),
                'e6': (4, 5),
                'e8': (4, 7),
                'f1': (5, 0),
                'f3': (5, 2),
                'f5': (5, 4),
                'f7': (5, 6),
                'g2': (6, 1),
                'g4': (6, 3),
                'g6': (6, 5),
                'g8': (6, 7),
                'h1': (7, 0),
                'h3': (7, 2),
                'h5': (7, 4),
                'h7': (7, 6),
            }

    # function for playing one turn of the game
    def play(self):
        # if it's the computer's turn
        if self.curr_state.player % 2 == self.computer:
            print("I'm thinking...")
            move_value = self.computer_move()
            if move_value < float('inf'):
                print('I know what to do!')
                self.curr_state.print_board()
        # if it's the player's turn
        else:
            valid = False
            intended_move = input('It is your turn, what move would you like to make?\n')
            while intended_move == '?':
                print(self.instructions)
                intended_move = input('It is your turn, what move would you like to make?\n')
            new_board = self.parse_move(intended_move, self.curr_state)
            valid = self.is_valid(new_board)
            while not valid:
                intended_move = input("I'm sorry, that is not a legal move.  Try again\n")
                if intended_move == '?':
                    intended_move = input(self.instructions)
                new_board = self.parse_move(intended_move, self.curr_state)
                valid = self.is_valid(new_board)
            self.curr_state = State(self.curr_state.player + 1, new_board)
            self.curr_state.print_board()
            print('good move, let me think for a second\n')
        self.curr_state.get_possible_actions()
        game_over = self.curr_state.is_terminal_state()
        if game_over:
            if self.curr_state.player % 2 == self.computer:
                print('Oh darn. You won.  You are pretty good at this.')
            else:
                print('YAYY I WON I AM THE BEST! MY INTELLIGENCE IS FAR SUPERIOR TO YOURS YOU DESPICABLE LITTLE HUMAN!')
            return True

    def computer_move(self):
        actions = self.curr_state.possible_actions
        if actions.qsize() != 0:
            max_value = -1*float('inf')
            while not actions.empty():
                this_state = actions.get()
                if self.game_size == 4:
                    action_value = self.minimax(this_state, 0, -1*float('inf'), float('inf'))
                else:
                    action_value = self.hminimax(this_state, 0, -1 * float('inf'), float('inf'))
                if action_value > max_value:
                    max_value = action_value
                    self.curr_state = this_state
                elif action_value == max_value:
                    # generate a random number between 1 and 100
                    choice_p = random.randint(1, 101)
                    # changes the move with a probability of 50%
                    if choice_p <= 50:
                        self.curr_state == this_state
            return max_value
        else:
            return float('inf')

    # when calling for the first time, minimax(curr_state,0,-inf,+inf)
    def minimax(self, state, depth, alpha, beta):
        # get queue of possible actions
        actions = state.get_possible_actions()
        # if you reach a draw and you're in an infinite search space, return
        if depth > 20:
            return state.get_utility(self.computer, True)
        # when you reach a terminal state, return the utility function on that state
        if state.is_terminal_state():
            u = state.get_utility(self.computer, False)
            return u
        # if the computer is the current player, run max
        if state.player % 2 == self.computer:
            # initialize best_val to the worst possible value so anything is better
            best_val = -1 * float('inf')
            # run through the list of actions
            while not actions.empty():
                value = self.minimax(actions.get(), depth + 1, alpha, beta)
                best_val = max(best_val, value)
                alpha = max(alpha, best_val)
                # beta is the upper bound on the min value and alpha is the lower bound on the max value
                if beta <= alpha:
                    break
            return best_val
        # if the computer is not the current player, run min
        if state.player % 2 != self.computer:
            # initialize best_val to the best possible value so anything is worse
            best_val = float('inf')
            while not actions.empty():
                value = self.minimax(actions.get(), depth+1, alpha, beta)
                best_val = min(best_val, value)
                beta = min(beta, best_val)
                if beta <= alpha:
                    break
            return best_val

    def hminimax(self, state, depth, alpha, beta):
        # get queue of possible actions
        actions = state.get_possible_actions()
        # when you reach a terminal state, return the utility function on that state
        if self.cutoff(state, depth):
            return self.eval(state)
        # if the computer is the current player, run max
        if state.player % 2 == self.computer:
            # initialize best_val to the worst possible value so anything is better
            best_val = -1 * float('inf')
            # run through the list of actions
            while not actions.empty():
                value= self.hminimax(actions.get(), depth + 1, alpha, beta)
                best_val = max(best_val, value)
                alpha = max(alpha, best_val)
                # beta is the upper bound on the min value and alpha is the lower bound on the max value
                if beta <= alpha:
                    break
            return best_val
        # if the computer is not the current player, run min
        if state.player % 2 != self.computer:
            # initialize best_val to the best possible value so anything is worse
            best_val = float('inf')
            while not actions.empty():
                value = self.hminimax(actions.get(), depth + 1, alpha, beta)
                best_val = min(best_val, value)
                beta = min(beta, best_val)
                if beta <= alpha:
                    break
            return best_val

    #heuristic function evaluates a state and returns the approximate value for that state
    #this heuristic counts the difference in the number of pieces of each team and weights kings more highly
    def eval(self, state):
        state_value = 0
        for i in range(self.game_size):
            for j in range(self.game_size):
                if state.board[i][j] != -5:
                    current_piece = state.board[i][j]
                    # if the computer is black
                    if current_piece == 1:
                        state_value += 1
                    elif current_piece == 2:
                        state_value -= 1
                    elif current_piece == 3:
                        state_value += 1.5
                    elif current_piece == 4:
                        state_value -= 1.5
        # if the computer is white, the state value is the opposite
        if self.computer % 2 == 0:
            state_value = state_value * -1
        return state_value

    def cutoff(self, state, depth):
        if depth > self.max_depth:
            return True
        elif state.is_terminal_state():
            return True
        else:
            return False

    def is_valid(self, board):
        possible_actions = self.curr_state.get_possible_actions()
        valid = False
        while not possible_actions.empty() and not valid:
            test_board = possible_actions.get().board
            if test_board == board:
                valid = True
        return valid

    def parse_move(self, intended_move, state):
        new_board = state.copy_board(state.board)
        string_array = intended_move.split()
        for t in range(len(string_array) // 2):
            correct_format = False
            while not correct_format:
                try:
                    start_space = string_array[0 + 2 * t]
                    operator = string_array[1 + 2 * t]
                    end_space = string_array[2 + 2 * t]
                    start_space = self.board_names[start_space]
                    end_space = self.board_names[end_space]
                    if operator == '-' or operator == 'X' or operator == 'x':
                        correct_format = True
                    else:
                        string_array = input(
                            'Your response was formatted incorrectly. Remember, use " - " to make a move and " x " to '
                            'make a capture.  Please enter the move you would like to make '
                            'with proper formatting\nExample: D1 X B3   D1 - C2  B5 X D3 X F1\n').split()
                except KeyError:
                    string_array = input('There was something wrong with your input.  Either the move is not possible, '
                                         'or it was formatted incorrectly.  Please enter the move you would like to make '
                                         'with proper formatting\nExample: D1 X B3   D1 - C2  B5 X D3 X F1\n').split()
            if operator == '-':
                new_board[end_space[0]][end_space[1]] = new_board[start_space[0]][start_space[1]]
                new_board[start_space[0]][start_space[1]] = 0
            else:
                new_board[end_space[0]][end_space[1]] = new_board[start_space[0]][start_space[1]]
                new_board[start_space[0]][start_space[1]] = 0
                new_board[(end_space[0]+start_space[0]) // 2][(end_space[1] + start_space[1]) // 2] = 0
        # Crown any kings
        for j in range(len(new_board)):
            # if black's turn
            if self.curr_state.player % 2 == 1:
                if new_board[len(new_board) - 1][j] == 1:
                    new_board[len(new_board) - 1][j] = 3
            else:  # if white's turn
                if new_board[0][j] == 2:
                    new_board[0][j] = 4
        return new_board
        # take the input and create a board