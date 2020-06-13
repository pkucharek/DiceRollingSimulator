import random


class Dice(object):
    def __init__(self):
        self._set_random_value()

    def set_value(self):
        self._set_random_value()

    def _set_random_value(self):
        self.value = random.randint(1, 6)
