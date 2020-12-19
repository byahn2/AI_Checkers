from State import State
from MoveMaker import MoveMaker
from Initialize import Initialize


def main():
    continue_play = True
    first = True
    while continue_play:
        initial = Initialize()
        play = initial.start_game(first)
        computer = initial.computer
        if play:
            move_finder = MoveMaker(initial.size, initial.initial_state, computer, initial.depth)
            game_over = False
            while not game_over:
                game_over = move_finder.play()
            print('Thank you for a very enjoyable game\n')
            play_again = input("If you would like to play again, enter 'y'\n")
        else:
            play_again = input("If you change your mind, just enter 'y'\n")
        if play_again == 'y':
            first = False
        else:
            continue_play = False
            print('Okay, have a nice day!\n')
main()

