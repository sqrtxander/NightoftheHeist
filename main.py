# imports
import random
from time import sleep


class Game:

    def __init__(self):  # declaring all the variables
        self.response = None
        self.action = None
        self.item = None
        self.inventory = []
        self.actions = ('help', 'inventory', 'actions', 'scan', 'walk', 'grab', 'drop', 'use')
        self.items = {(0, 0): ['wire', 'crowbar'], (1, 0): ['rock', 'key'],  # level 0 items
                      (1, 1): [], (1, 2): [], (1, 3): [],  # level 1 items
                      (0, 2): [],  # level 2 items
                      (2, 3): [], (3, 3): [],  # level 3 items
                      (3, 2): []}  # level 4 items
        self.plx, self.ply = 0, 0  # player's x and y coordinates
        self.unlocked_lvls = [True, False, False, False, False]

        self.vault_code = str(random.randint(0000, 9999)).zfill(4)  # generates a 4 digit code from 0000 to 9999

        print(self.vault_code)

        self.wrong_till_over = 5

    def describe_area(self):
        general_desc = {(0, 0): '''South west of bank''',
                        (1, 0): 'South of bank. The door is firmly locked',
                        # level 0 descriptions
                        (1, 1): 'Entrance of bank', (1, 2): 'Entrance of bank, the counter is on your left',
                        (1, 3): 'Entrance of bank, there is a hallway above and to the right of you',
                        # level 1 descriptions
                        (0, 2): 'You are behind the counter, there is a keypad with a 4 digit code entry system',
                        # level 2 descriptions
                        (2, 3): '', (3, 3): '',  # level 3 descriptions
                        (3, 2): ''}  # level 4 descriptions

        # takes list and puts it in the form 'a 0, a 1, a 2 and a 3'
        items_list = ['a ' + i for i in self.items[(self.plx, self.ply)]]  # starts each item with the string 'a '
        if len(items_list) == 1:
            items_str = items_list[0]
        elif len(items_list) == 0:
            items_str = 'nothing'

        else:
            items_str = ', '.join(items_list[:-1]) + ' and ' + items_list[-1]

        desc_text = general_desc[(self.plx, self.ply)] + ', you see ' + items_str
        print(desc_text)

    def help_(self):
        if self.item is None:  # if self.item not provided i.e. user only typed "help"
            print('This is the general help')
            sleep(1)
            print('for action specific help, use this function in the form "help <action>"')
            sleep(1)
            print('For the list of actions you can do, type "actions"')
            sleep(1)
            print('When you see the following line:')
            sleep(1)
            print('>')
            sleep(1)
            print('You are being prompted to type something')

        elif self.item not in self.actions:
            print(f'Action "{self.item}" not recognised')

        elif self.item == 'walk':
            print('The walk action takes the form of "walk <direction>"')
            sleep(1)
            print('The valid directions are "North", "East", "South", and "West"')

        elif self.item == 'grab':
            print('The grab action takes the form of "grab <item>"')
            sleep(1)
            print('The items that are around you are told to you after walking or alternatively you can use the '
                  '"scan" action')

        elif self.item == 'drop':
            print('The drop action takes the form of "drop <item>"')
            sleep(1)
            print('It will drop an item from your inventory into the current area')

        elif self.item == 'inventory':
            print('The inventory action takes the form of "inventory"')
            sleep(1)
            print('It will tell you what you have in your inventory')

        elif self.item == 'scan':
            print('The scan action takes the form of "scan"')
            sleep(1)
            print('It will inform you of your surroundings and tell you what items are around.')

        elif self.item == 'use':
            print('The use function takes the form of "use <item>"')
            sleep(1)
            # TODO

        elif self.item == 'help':
            print('The help function takes the form of "help <action>"')
            sleep(1)
            print('If there is no action provided, it will tell you the general help')
            sleep(1)
            print('It will tell you how the action is used and what it does')

    def walk(self):
        map_spaces = {(0, 0): 0, (1, 0): 0,
                      (1, 1): 1, (1, 2): 1, (1, 3): 1,
                      (0, 2): 2,
                      (2, 3): 3, (3, 3): 3,
                      (3, 2): 4}

        dirs = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0),
                'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0)}

        if self.item is None:
            print('This action is used in the form "walk <direction>"')

        elif self.item not in dirs:
            print(f'Direction "{self.item}" isn\'t recognised')

        else:
            dx, dy = dirs[self.item]
            if (self.plx + dx, self.ply + dy) in map_spaces:  # if space is on the map
                if self.unlocked_lvls[map_spaces[(self.plx + dx, self.ply + dy)]]:  # if level of space is unlocked
                    self.plx += dx
                    self.ply += dy

                    self.describe_area()
                else:
                    print('You have not unlocked this area yet')
            else:
                print('You walked into a wall')

    def grab(self):  # grab action moves item from the areas item list to players inventory
        if self.item is None:
            print('This action is used in the form "grab <item>"')
        elif self.item in self.items[(self.plx, self.ply)]:  # if the item is in the room
            self.items[(self.plx, self.ply)].remove(self.item)
            self.inventory.append(self.item)
            print(f'You picked up the {self.item}')
        else:  # if the item isn't there to grab.
            print(f'There isn\'t "{self.item}" in the area')

    def drop(self):  # drop action moves item from your inventory to the areas item list
        if self.item is None:
            print('This action is used in the form "drop <item>"')
        elif self.item in self.inventory:  # if the item is in your inventory
            self.items[(self.plx, self.ply)].append(self.item)
            self.inventory.remove(self.item)
            print(f'You dropped the {self.item}')
        else:
            print(f'There isn\'t "{self.item}" in your inventory')

    def use(self):
        # TODO
        if self.item not in self.inventory:
            print(f'You do not have a {self.item} to use')
            return

        obj = input(f'What would you like to use the {self.item} on?\n').strip().lower()

        if (self.plx, self.ply) == (1, 0):
            if self.item == 'wire':
                if 'lock' in obj:
                    if not self.unlocked_lvls[1]:  # if level 1 not unlocked
                        print('You manage to pick the lock. The door creaks open.')
                        self.unlocked_lvls[1] = True
                        self.unlocked_lvls[3] = True
                    else:
                        print('You have already unlocked the door')
                else:
                    print(f'You can\'t use the {self.item} here')

        elif (self.plx, self.ply) == (1, 2):
            if self.item == 'key':
                if 'counter' in obj:
                    print('The key worked, the counter is open')
                    self.unlocked_lvls[2]\
                        = True
                else:
                    print(f'You can\'t use {self.item} here')

        else:
            print(f'You can\'t use {self.item} here')

    def print_inventory(self):
        if not self.inventory:  # if inventory is empty
            print('There are no items in your inventory.')
        else:
            print('The items currently in your inventory are:')
            print(', '.join(self.inventory))

    def print_actions(self):
        print('The recognised actions are:')
        print(', '.join(self.actions))

    def parse_inp(self):  # TODO
        response_list = self.response.lower().strip().split(' ')  # get a list of the words in the input

        try:
            self.action = response_list[0]
            self.item = response_list[1]
        except IndexError:  # if there is less than 2 words in the input
            self.action = response_list[0]
            self.item = None

        if self.action == 'help':
            self.help_()

        elif self.action == 'inventory':
            self.print_inventory()

        elif self.action == 'actions':
            self.print_actions()

        elif self.action == 'scan':
            self.describe_area()

        elif self.action == 'drop':
            self.drop()

        elif self.action == 'walk':
            self.walk()

        elif self.action == 'grab':
            self.grab()

        elif self.action == 'use':
            self.use()

        else:
            self.other_inps()

    def other_inps(self):
        if (self.plx, self.ply) == (0, 2):
            if 'code' in self.response.lower():
                code_guess = input('Enter code: ')
                if code_guess == self.vault_code:
                    self.unlocked_lvls[4] = True
                    print('Vault unlocked')
                elif 'cancel' in code_guess:
                    self.describe_area()
                else:
                    print('Incorrect code, security called')
                    self.wrong_till_over -= 1

        elif self.action not in self.actions:
            print(f'Action "{self.action}" not recognised')

    def main(self):
        #     print('Welcome to Night of the Heist.')
        #     sleep(1.5)
        #     print('When you see the following line:')
        #     sleep(1.5)
        #     print('>')
        #     sleep(1.5)
        #     print('you are being prompted to input something.')
        #     sleep(1.5)
        #     print('''If at any point during the game you don't know what you are doing,
        # you can simply input the phrase "help" when you are able to.''')
        #     sleep(3)
        #     print('''if you would like help now, enter the phrase "help",
        # otherwise, if you know what you're doing, press enter.''')

        self.describe_area()
        while True:
            self.response = input('> ')
            self.parse_inp()


if __name__ == '__main__':
    game = Game()
    game.main()
