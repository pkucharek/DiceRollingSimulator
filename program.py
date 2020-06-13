class Program(object):
    def __init__(self, dice):
        self.dice = dice
        self.exit = False

    def ask_user(self):
        print(f'This is your number: {self.dice.value}, should I roll again?')

    def get_user_input(self):
        choice = str(input()).lower()
        if choice == "yes":
            self.dice.set_value()
        elif choice == "no":
            self.exit = True
        else:
            print("Type 'yes' or 'no'!")

    def __str__(self):
        return f'self.dice.value = {self.dice.value}, self.exit = {self.exit}\n'
