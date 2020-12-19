'''This is the class State.  States are the nodes of the game tree.  A state is defined by the board (a 2x2 array),
which player's turn it is, and  '''

from queue import Queue

class State(object):
    # initialize State
    def __init__(self, player, board):
        self.player = player
        self.board = board
        self.max_caps = 0
        # if all 12 pieces can make 4 moves, then the max number of moves is 48
        self.possible_actions = Queue(48)
        # a dictionary of what each integer should be printed as
        self.board_displays = {
            '-5': '-',
            '0': ' ',
            '1': 'b',
            '2': 'w',
            '3': 'B',
            '4': 'W'
        }

    # copy the board so that you have a completely new object
    def copy_board(self, a):
        b = [row[:] for row in a]
        return b

    # print the board with X's in squares you can't go in, b's for black pawns, B's for black kings, w's for white pawns, and W's for white kings and blank spaces for zeros
    def print_board(self):
        if len(self.board) == 4:
            print('\n       1     2     3     4')
            divider = '\n    __________________________\n'
        else:
            print('\n       1     2     3     4     5     6     7     8')
            divider = '\n    __________________________________________________\n'
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(len(self.board)):
            print(divider)
            print(letters[i]+'   |', end='')
            for j in range(len(self.board)):
                print('  ' + self.board_displays[str(self.board[i][j])] + '  |', end='')
        print(divider)

    # returns a queue of all possible actions
    def get_possible_actions(self):
        capture_possible = False  # boolean that is true only if a capture can be made
        for i in range(len(self.board)): # go through each square on the board
            for j in range(len(self.board[i])):
                if self.board[i][j] != -5:
                    # check to see if any captures can be made.  Return none if none can be made, return the max number of captures if any can be made
                    capture = self.check_capture(self.board, i, j, 0)
                    if capture is not None:
                        capture_possible = True  # if a capture can be made, set capture possible to true
        # if no captures can be made, explore what non-capture moves can be made
        if not capture_possible:
            for i in range(len(self.board)):  # go through each square on the board
                for j in range(len(self.board[i])):
                    if self.board[i][j] != -5:
                        self.check_move(i, j)
        return self.possible_actions  # return queue of possible actions

    # function to check if a capture can be made by a given player on a given board from a given square (i,j) while keeping track of the current number of captures and the maximum number of captures that have been made so far on the board
    def check_capture(self, board, i, j, num_caps):
        capture_made = False
        columns = [j + 1, j - 1]
        landing_columns = [j + 2, j - 2]
        # if black's move
        if self.player % 2 == 1:
            p = i+1  # pawns can move forwards
            lp = i + 2  # pawns landing piece is 2 spaces forwards
            k = i-1  # kings can also move backwards
            lk = i - 2  # kings can land 2 spaces backwards
            pawn = 1  # black's pawns are represented by a 1
            king = 3  # black's kings are represented by a 3
            enemy_pawn = 2  # white's pawns are represented by a 2
            enemy_king = 4  # white's king's are represented by a 4
            other_end = len(board)-1  # black's other end of the board is len(board)-1
        else:  # white's move
            p = i - 1  # pawns can move forwards
            lp = i - 2  # pawns landing piece is 2 spaces forwards
            k = i + 1  # kings can also move backwards
            lk = i + 2  # kings can land 2 spaces backwards
            pawn = 2  # white's pawns are represented by a 2
            king = 4  # white's king's are represented by a 4
            enemy_pawn = 1  # black's pawns are represented by a 1
            enemy_king = 3  # black's kings are represented by a 3
            other_end = 0  # white's other end of the board is len(board)-1
        if board[i][j] == king:  # if square (i,j) contains a king
            # check move to the back left and to the back right
            for move in range(len(columns)):
                c = columns[move]  # column being jumped
                lc = landing_columns[move]  # landing column
                if 0 <= lk < len(board) and 0 <= lc < len(board):  # if the landing square exists
                    if (board[k][c] == enemy_pawn or board[k][c] == enemy_king) and (board[lk][lc] == 0):  # and a capture is possible
                        # the number of possible captures increases
                        capture_made = True
                        num_caps += 1
                        if num_caps > self.max_caps:
                            # if a longer line of captures is found, update the maximum number of captures and remove all shorter lines of captures
                            self.max_caps = num_caps
                            while not self.possible_actions.empty():
                                self.possible_actions.get()
                        # create a new board assuming the capture was made
                        new_board = self.copy_board(board)
                        new_board[k][c] = 0
                        new_board[lk][lc] = new_board[i][j]
                        new_board[i][j] = 0
                        # check if another capture can be made
                        next_cap = self.check_capture(new_board, lk, lc, num_caps)
                        if next_cap is not None:
                            num_caps = num_caps - 1
                        # when no more captures can be made and if this is the move with the most captures
                        if next_cap is None and num_caps == self.max_caps:
                            self.possible_actions.put(State(self.player + 1, new_board))  # add the capture to the list of moves
        if board[i][j] == king or board[i][j] == pawn:  # if the square i,j contains a piece
            for move in range(len(columns)):  # check moves to the front left and front right
                c = columns[move]  # column being jumped
                lc = landing_columns[move]  # landing column
                if 0 <= lp < len(board) and 0 <= lc < len(board):  # if the landing square exists
                    if (board[p][c] == enemy_pawn or board[p][c] == enemy_king) and (board[lp][lc] == 0):  # and if a capture is possible
                        capture_made = True
                        num_caps += 1  # the number of possible captures increases
                        if num_caps > self.max_caps:
                            # if a longer line of captures is found, remove all shorter lines of captures
                            self.max_caps = num_caps
                            while not self.possible_actions.empty():
                                self.possible_actions.get()
                        # create a new board assuming the capture was made
                        new_board = self.copy_board(board)
                        new_board[p][c] = 0
                        new_board[lp][lc] = new_board[i][j]
                        new_board[i][j] = 0
                        # check if another capture can be made
                        next_cap = self.check_capture(new_board, lp, lc, num_caps)
                        if next_cap is not None:
                            num_caps = num_caps -1
                        # when no more captures can be made and if this is the move with the most captures
                        if next_cap is None and num_caps == self.max_caps:
                            last_row = len(new_board)
                            # turn all of the pieces that might be kings into kings
                            for square in range(last_row):
                                if new_board[other_end][square] == pawn:
                                    new_board[other_end][square] = king
                            self.possible_actions.put(State(self.player+1, new_board)) # add the capture to the list of moves
        if not capture_made:
            # if no new captures were made, return null
            return None
        else:
            # if captures have been made, return max caps
            return num_caps

    # function that checks what moves are possible for a given player on a given board from a given square (i,j) and adds them to the possible actions queue
    def check_move(self, i, j):
        # columns is an array containing a move left and a move right
        columns = [j + 1, j - 1]
        if self.player % 2 == 1:  # if black's move
            p = i+1  # pawns can move forwards
            k = i-1  # kings can also move backwards
            pawn = 1  # black's pawns are represented by a 1
            king = 3  # black's kings are represented by a 3
            other_end = len(self.board)-1  # the other end of the board for black is i = len(board)-1
        else:   # if white's move
            p = i-1  # pawns can move forwards
            k = i+1  # kings can also move backwards
            pawn = 2  # white's pawns are represented by a 2
            king = 4  # white's kings are represented by a 4
            other_end = 0
        if self.board[i][j] == king:  # if there is a king in the square i,j, start by checking backwards moves
            for d in columns:  # loop through checking left and checking right
                if 0 <= k < len(self.board) and 0 <= d < len(self.board):  # if the potential landing square exists
                    if self.board[k][d] == 0:  # and the landing square is free
                        # update board
                        new_board = self.copy_board(self.board)
                        new_board[k][d] = new_board[i][j]
                        new_board[i][j] = 0
                        # add to list
                        self.possible_actions.put(State(self.player+1, new_board))
        # if there is a piece in the square i,j
        if self.board[i][j] == pawn or self.board[i][j] == king:
            for d in columns:
                if 0 <= p < len(self.board) and 0 <= d < len(self.board):  # if the potential landing square exists
                    if self.board[p][d] == 0:  # and the landing square is free
                        # update board
                        new_board = self.copy_board(self.board)
                        if p == other_end:
                            new_board[p][d] = king
                        else:
                            new_board[p][d] = new_board[i][j]
                        new_board[i][j] = 0
                        # add to list
                        self.possible_actions.put(State(self.player+1, new_board))

    def get_utility(self, computer, draw):
        # if it's a draw, utility = 0
        if draw:
            return 0
        # if the player that has no moves is the computer, the computer has lost. return -1
        elif computer == self.player % 2:
            return -1
        # if the player that has no moves is the person, the computer has won. return +1
        else:
            return 1

    def is_terminal_state(self):
        # it's a terminal state if no more actions can be made
        if self.possible_actions.empty():
            return True
        else:
            return False

    def is_draw(self):
        print('It is a draw :(')

    def _repr_(self):
        return self._str_()
