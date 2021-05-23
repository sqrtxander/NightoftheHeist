# imports
from time import sleep


def help_():
    # TODO
    print('When you see the following line:')
    print('>')
    print('you are being prompted to input something.')
    sleep(2)
    print('''For the best chance that your input is understood, use a two word input
with the first word being an action and the second word being the subject.
e.g. grab rock, use glass''')
    sleep(2)
    print('''For a list of the recognised actions, type \'actions\'''')


class Game:

    def __init__(self):
        self.action = None
        self.noun = None
        self.response = None
        self.inventory = []
        self.actions = ('walk', 'grab', 'view', 'use')
        self.objects = [['rock', 'key'],  # level 0 objects
                        ['bag', 'soap']]  # level 1 objects
        self.plx, ply = 0, 0  # player's x and y coordinates
        self.level = 0

        self.main()

    def grab(self):
        if self.noun in self.objects[self.level]:
            self.objects[self.level].remove(self.noun)
            self.inventory.append(self.noun)
            print()
        else:  # if the object isn't recognised
            print(f'Unknown object {self.noun}')

    def print_inventory(self):
        if not self.inventory:  # if inventory is empty
            print('There are no items in your inventory.')
        else:
            print('The items currently in your inventory are:')
            for i in self.inventory:
                print(i)

    def verbs(self):
        print('The recognised verbs are:')
        for i in self.actions:
            print(i)

    def parse_inp(self):  # TODO
        if 'help' in self.response.lower():
            help_()
        elif 'inventory' in self.response.lower():
            self.print_inventory()
            return  # stop the rest of the function from executing

        response_list = self.response.lower().strip().split(' ')  # get a list of the words in the input

        try:
            self.action = response_list[0]
            self.noun = response_list[1]
        except IndexError:  # if there is less than 2 words in the input
            print(f'Unknown action {self.response}')
            return  # stop the rest of the function from executing

        if self.action not in self.actions:
            print(f'Unknown action {self.action}')

        elif self.action == 'grab':  # grab action moves object from the specific levels list to players inventory
            self.grab()

    def main(self):
        print('Welcome to Night of the Heist.')
        sleep(1.5)
        print('When you see the following line:')
        sleep(1.5)
        print('>')
        sleep(1.5)
        print('you are being prompted to input something.')
        sleep(1.5)
        print('''If at any point during the game you don't know what you are doing,
you can simply input the phrase "help" when you are able to.''')
        sleep(3)
        print('''if you would like help now, enter the phrase "help", 
otherwise, if you know what you're doing, press enter.''')

        self.response = input('>')
        self.parse_inp()
        while True:
            self.response = input('>')
            self.parse_inp()


if __name__ == '__main__':  # currently test code

    game = Game()
