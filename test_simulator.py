import mock

from dice import Dice
from program import Program
import pytest


@pytest.fixture
def dice():
    return Dice()


@pytest.fixture
def program(dice):
    return Program(dice)


@pytest.fixture
def dices_array(dice):
    return [dice] * 1000


@pytest.fixture
def programs_array():
    return [Program(Dice()) for i in range(1000)]


def is_dice_in_range(dice):
    return 1 <= dice.value <= 6


def test_dices(dices_array):
    for dice in dices_array:
        assert is_dice_in_range(dice)


def test_setting_dice_values(dices_array):
    for dice in dices_array:
        dice.set_value()
        assert is_dice_in_range(dice)


def test_program(programs_array, capsys):
    for program in programs_array:
        program.ask_user()
        captured = capsys.readouterr()
        assert captured.out == f'This is your number: {program.dice.value}, should I roll again?\n'


def test_roll_flow(programs_array, capsys):
    for program in programs_array:
        with mock.patch('builtins.input', return_value="yes"):
            program.get_user_input()
            assert program.exit is False
        with mock.patch('builtins.input', return_value="YeS"):
            program.get_user_input()
            assert program.exit is False
        with mock.patch('builtins.input', return_value="no"):
            program.get_user_input()
            assert program.exit is True
        with mock.patch('builtins.input', return_value="nO"):
            program.get_user_input()
            assert program.exit is True
        with mock.patch('builtins.input', return_value="asdqwer"):
            program.get_user_input()
            captured = capsys.readouterr()
            assert captured.out == "Type 'yes' or 'no'!\n"
