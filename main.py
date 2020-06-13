from program import Program
from dice import Dice


def main():
    program = Program(Dice())
    while not program.exit:
        program.ask_user()
        program.get_user_input()


if __name__ == '__main__':
    main()
