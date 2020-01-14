import os
from functools import partial


def get_choice():
    choice = input("Your choice: ")
    breakline()
    return choice


def breakline():
    print('-' * 120)


def clrscr():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def take_input(List, *args):
    
    assert len(args) == len(List)
    breakline()
    for i, elem in enumerate(List):
        print(f'{i + 1}: {elem}')
    breakline()

    choice = get_choice()
    assert choice.isdigit() and int(choice) in range(1, len(List) + 1)

    choice = int(choice) - 1
    args[choice]()
    return True


# def banner_print(*args, **kwargs):
#     print(*[pyfiglet.figlet_format(x, **kwargs) for x in args])


def main():
    take_input(['sup', 'exit'], [print, "Hey", "Sup?"], [exit])


if __name__ == '__main__':
    main()