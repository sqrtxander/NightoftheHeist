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
        self.obj = None
        self.response = None
        self.inventory = []
        self.actions = ('walk', 'grab', 'drop', 'use')
        self.objects = [['rock', 'key'],  # level 0 objects
                        ['bag', 'soap']]  # level 1 objects
        self.plx, self.ply = 0, 0  # player's x and y coordinates
        self.level = 0

    def walk(self):

        map_spaces = ((0, 0), (0, 1), (-1, 1), (1, 1))

        dirs = {'up': (0, 1), 'right': (1, 0),
                'down': (0, -1), 'left': (-1, 0)}

        if self.obj not in dirs:
            print(f'Unknown direction {self.obj}')

        else:
            dx, dy = dirs[self.obj]
            if (self.plx + dx, self.ply + dy) in map_spaces:
                self.plx += dx
                self.ply += dy
                print(f'You walked {self.obj}')
                print((self.plx, self.ply))
            else:
                print('You walked into a wall.')

    def grab(self):  # grab action moves object from the areas object list to players inventory
        if self.obj in self.objects[self.level]:  # if the object is in the room
            self.objects[self.level].remove(self.obj)
            self.inventory.append(self.obj)
            print(f'You picked up {self.obj}.')
        else:  # if the object isn't there to grab.
            print(f'There isn\'t "{self.obj}" in the area')

    def drop(self):  # drop action moves object from your inventory to the areas object list
        if self.obj in self.inventory:  # if the object is in your inventory
            self.objects[self.level].append(self.obj)
            self.inventory.remove(self.obj)
            print(f'You dropped {self.obj}')
        else:
            print(f'There isn\'t "{self.obj}" in your inventory')

    def use(self):
        # TODO
        pass

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
            self.obj = response_list[1]
        except IndexError:  # if there is less than 2 words in the input
            print(f'Unknown action {self.response}')
            return  # stop the rest of the function from executing

        if self.action not in self.actions:
            print(f'Unknown action {self.action}')

        elif self.action == 'grab':
            self.grab()

        elif self.action == 'drop':
            self.drop()

        elif self.action == 'walk':
            self.walk()

    def main(self):
#         print('Welcome to Night of the Heist.')
#         sleep(1.5)
#         print('When you see the following line:')
#         sleep(1.5)
#         print('>')
#         sleep(1.5)
#         print('you are being prompted to input something.')
#         sleep(1.5)
#         print('''If at any point during the game you don't know what you are doing,
# you can simply input the phrase "help" when you are able to.''')
#         sleep(3)
#         print('''if you would like help now, enter the phrase "help",
# otherwise, if you know what you're doing, press enter.''')

        while True:
            self.response = input('>')
            self.parse_inp()


if __name__ == '__main__':
    game = Game()
    game.main()
