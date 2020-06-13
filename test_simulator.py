from typing import List

import mock

from dice import Dice
from program import Program
import pytest


@pytest.fixture
def dice() -> Dice:
    return Dice()


@pytest.fixture
def program(dice: Dice) -> Program:
    return Program(dice)


@pytest.fixture
def dices_array(dice: Dice) -> List[Dice]:
    return [dice] * 1000


@pytest.fixture
def programs_array() -> List[Program]:
    return [Program(Dice()) for i in range(1000)]


def is_dice_in_range(dice: Dice):
    return 1 <= dice.value <= 6


def test_dices(dices_array: List[Dice]):
    for dice in dices_array:
        assert is_dice_in_range(dice)


def test_setting_dice_values(dices_array: List[Dice]):
    for dice in dices_array:
        dice.set_value()
        assert is_dice_in_range(dice)


def test_program(programs_array: List[Program], capsys):
    for program in programs_array:
        program.ask_user()
        captured = capsys.readouterr()
        assert captured.out == f'This is your number: {program.dice.value}, should I roll again?\n'


@pytest.mark.parametrize("text, expected_exit, expected_text", [
    ("yes", False, ''),
    ("YeS", False, ''),
    ("asdqwer", False, "Type 'yes' or 'no'!\n"),
    ("no", True, ''),
    ("nO", True, ''),
])
def test_roll_flow(programs_array: List[Program], capsys,
                   text: str, expected_exit: bool,
                   expected_text: str):
    for program in programs_array:
        with mock.patch('builtins.input', return_value=text):
            program.get_user_input()
            captured = capsys.readouterr()
            assert program.exit is expected_exit
            assert captured.out == expected_text
