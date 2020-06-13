import random


class Dice(object):
    def __init__(self) -> None:
        self._set_random_value()

    def set_value(self) -> None:
        self._set_random_value()

    def _set_random_value(self) -> None:
        self.value = random.randint(1, 6)
