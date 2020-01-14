from N_queens import N_queens
import pickle
from func import breakline, clrscr, take_input
import random
import os
from termcolor import colored, cprint

fName = "outputs.pkl"


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if not board[i][j]:
                cprint('◻️', 'magenta', end=" ")
            else:
                cprint('Q', 'green', end=" ")
        print()


def gen():
    cprint('Generating The Outputs to 20 queen problem', 'green')
    breakline()
    cprint('Press ctrl+c To stop generating and save the solutions to a file.', 'yellow')
    breakline()
    input('Press Enter To Begin.')
    breakline()
    try:
        S = N_queens(20).solve()
    except KeyboardInterrupt:
        print('Saving The Generated Outputs!')
    breakline()
    print(f'Saving The Output in {fName}')
    print(len(S))
    pickle.dump(S, open(fName, 'wb'))
    breakline()
    cprint('Saved!', 'green')
    breakline()
    print('A Solution From The saved ones is:')
    print_board(random.choice(list(S.values())))
    breakline()


def prev():
    cprint('Loading the previously saved outputs!', 'yellow')
    if not os.path.isfile(fName):
        print('No previously saved outputs exist! Generating Them!')
        gen()
    solutions = pickle.load(open(fName, 'rb'))
    N = len(solutions)
    N_Outputs = int(input(f'How  Many Outputs Do You Wanna Print? There are currently {N} outputs stored.\nChoice: '))
    assert N_Outputs < N, "Can't be bigger than the number of outputs!"
    for _ in range(N_Outputs):
        temp = random.randint(1, N)
        cprint(f'{temp}th Solution out of {N}', 'green')
        print_board(solutions[temp])


def main():
    breakline()
    cprint('WELCOME TO 20 QUEENS PROBLEM!', 'yellow')
    take_input(['Generate Outputs', 'Print Previously Generated Ones'], gen, prev)


if __name__ == '__main__':
    main()