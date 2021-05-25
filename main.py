# imports
from time import sleep


class Game:

    def __init__(self):
        self.action = None
        self.obj = None
        self.response = None
        self.inventory = []
        self.actions = ('help', 'inventory', 'walk', 'grab', 'drop', 'use')
        self.objects = [['rock', 'key'],  # level 0 objects
                        ['bag', 'soap']]  # level 1 objects
        self.plx, self.ply = 0, 0  # player's x and y coordinates
        self.level = 0
        self.max_level = 0

    def help_(self):
        # TODO

        if self.obj is None:
            print('This is the general help')
            sleep(1)
            print('for action specific help, use this function in the form "help <action>"')
            # TODO
            sleep(1)
            print('When you see the following line:')
            sleep(1)
            print('>')
            sleep(1)
            print('You are being prompted to input something')
            sleep(1)
            print('For the list of actions, input "actions"')
            sleep(1)
            print()

        elif self.obj not in self.actions:
            print(f'Action {self.obj} not recognised')

        elif self.obj == 'walk':
            print('The walk action takes the form of "walk <direction>"')
            sleep(1)
            print('The valid directions are "up", "down", "left", and "right"')

        elif self.obj == 'grab':
            print('The grab action takes the form of "grab <object>"')
            sleep(1)
            print('The objects that are around you will be told to you') # TODO

        elif self.obj == 'inventory':
            print('The inventory action takes the form of "inventory"')
            sleep(1)
            print('It will tell you what you have in your inventory')

        elif self.obj == 'drop':
            print('The drop action takes the form of "drop <object>"')
            sleep(1)
            print('It will drop an item from your inventory into the current area')

    def walk(self):
        if self.obj is None:
            print('This action is used in the form "walk <direction>"')

        map_spaces = {(0, 0): 0, (1, 0): 0,
                      (1, 1): 1, (1, 2): 1, (1, 3): 1,
                      (0, 2): 2,
                      (2, 3): 3, (3, 3): 3,
                      (3, 2): 4}

        dirs = {'up': (0, 1), 'right': (1, 0),
                'down': (0, -1), 'left': (-1, 0)}

        if self.obj not in dirs:
            print(f'Unknown direction {self.obj}')

        else:
            dx, dy = dirs[self.obj]
            if (self.plx + dx, self.ply + dy) in map_spaces:  # if space is on the map
                if map_spaces[(self.plx + dx, self.ply + dy)] <= self.max_level:  # if level of space is unlocked
                    self.plx += dx
                    self.ply += dy
                    print(f'You walked {self.obj}')
                    print((self.plx, self.ply))

                    self.level = map_spaces[(self.plx, self.ply)]

                    print(self.level)  # update level you are in
                else:
                    print('You do not have the ability to go here yet.')
            else:
                print('You walked into a wall.')

    def grab(self):  # grab action moves object from the areas object list to players inventory
        if self.obj is None:
            print('This action is used in the form "grab <object>"')
        if self.obj in self.objects[self.level]:  # if the object is in the room
            self.objects[self.level].remove(self.obj)
            self.inventory.append(self.obj)
            print(f'You picked up {self.obj}.')
        else:  # if the object isn't there to grab.
            print(f'There isn\'t "{self.obj}" in the area')

    def drop(self):  # drop action moves object from your inventory to the areas object list
        if self.obj is None:
            print('This action is used in the form "drop <object>"')
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

    def print_actions(self):
        print('The recognised actions are:')
        for i in self.actions:
            print(i)

    def parse_inp(self):  # TODO

        response_list = self.response.lower().strip().split(' ')  # get a list of the words in the input

        try:
            self.action = response_list[0]
            self.obj = response_list[1]
        except IndexError:  # if there is less than 2 words in the input
            # print(f'Unknown action {self.response}')
            self.action = response_list[0]
            self.obj = None

        if self.action not in self.actions:
            print(f'Action {self.action} not recognised')

        if self.action == 'help':
            self.help_()

        elif self.action == 'inventory':
            self.print_inventory()

        elif self.action == 'actions':
            self.print_actions()

        elif self.action == 'drop':
            self.drop()

        elif self.action == 'walk':
            self.walk()

        elif self.action == 'grab':
            self.grab()


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
