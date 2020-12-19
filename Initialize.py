from State import State


class Initialize:
    def __init__(self):
        self.initial_state = State(1, [])
        self.computer = 0
        self.size = 0
        self.depth = 0
        self.board_displays = {
            '-5': '-',
            '0': ' ',
            '1': 'b',
            '2': 'w',
            '3': 'B',
            '4': 'W'
        }

    def start_game(self, first):
        continue_play = True
        if first:
            play = input('Hey, do you wanna play some checkers? (y/n)\n')
            first = False
            if play == 'n' or play == 'N' or play == 'no' or play == 'No' or play == 'No thanks':
                print('Oh that is too bad :( I guess I will just sit and contemplate my meaningless '
                      'artificial existence until someone decides to play with me\n')
                continue_play = False
            elif play == 'y' or play == 'Y' or play == 'yes' or play == 'Yes' or play == 'Yes please':
                continue_play = True
                self.get_input()
            else:
                print('I am not quite sure what you meant by that, could you give a more definitive answer? (y/n)\n')
                self.start_game(first)
        else:
            self.get_input()
        return continue_play

    def get_input(self):
        self.size = int(input('Sick!  Do you want to play on a 4x4 board or a full sized 8x8? (4/8)\n'))
        while self.size != 4 and self.size != 8:
            self.size = int(input('I am so sorry, I do not think we have that board size.  '
                                  'Could you please choose either 4 or 8?\n'))
        if self.size == 4:
            self.depth = 0
            self.initial_state.board = [[-5, 1, -5, 1], [0, -5, 0, -5], [-5, 0, -5, 0], [2, -5, 2, -5]]
        else:
            self.initial_state.board = [[-5, 1, -5, 1, -5, 1, -5, 1], [1, -5, 1, -5, 1, -5, 1, -5], [-5, 0, -5, 0, -5, 0, -5, 0],
                          [0, -5, 0, -5, 0, -5, 0, -5], [-5, 0, -5, 0, -5, 0, -5, 0], [0, -5, 0, -5, 0, -5, 0, -5],
                          [-5, 2, -5, 2, -5, 2, -5, 2], [2, -5, 2, -5, 2, -5, 2, -5]]

            self.depth = int(input('How deep would you like me to search when making a move? (int 2-10)\n'
                                   'Note, a depth of 6 will answer in ~15s, a depth of 7 will answer in ~30s, '
                                   'and a depth of 8 will answer in ~90s\n'))
            while 2 < self.depth and self.depth > 10:
                self.depth = int(input('I do not think I can do that.  Could you give me a number between 2 and 10?\n'))
        color = input('Oh I cannot wait! This will be so much fun.  Do you want to play as black or as white?  '
                      'Black goes first (b/w)\n')
        while color != 'b' and color != 'w' and color != 'B' and color != 'W' and color != 'black' and \
                color != 'white' and color != 'Black' and color != 'White':
            color = input('That is a cool color, but unfortunately on this board you can only play as '
                          'black or white. (b/w)\n')
        if color == 'b' or color == 'B' or color == 'black' or color == 'Black':
            self.computer = 0
        else:
            self.computer = 1