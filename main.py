# imports
from time import sleep


class Game:

    def __init__(self):
        self.action = None
        self.obj = None
        self.response = None
        self.inventory = []
        self.actions = ('help', 'inventory', 'actions', 'scan', 'walk', 'grab', 'drop', 'use')
        # self.objects = [['rock', 'key', 'poo', '4', '5'],  # level 0 objects
        #                 ['bag', 'soap']]  # level 1 objects

        self.objects = {(0, 0): ['wire', 'crowbar'], (1, 0): ['rock', 'key']  # level 0 objects
                        }
        self.plx, self.ply = 0, 0  # player's x and y coordinates
        self.lvl = 0
        self.max_lvl = 0

    def describe_area(self):
        general_desc = {(0, 0): 'You are outside of the bank, you see the entrance above and to the right of you',
                        (1,
                         0): 'You are outside of the bank, there is an area to your left. The entrance is locked and above you'
                        # level 0 descriptions
                        }

        # objects_list = ', '.join(self.objects[self.lvl][:-1]) + ' and ' + self.objects[self.lvl][-1]

        # takes list and puts it in the form 'a 0, a 1, a 2 and a 3'
        objs_list = ['a ' + i for i in self.objects[(self.plx, self.ply)]]
        if len(objs_list) == 1:
            objects_str = objs_list[0]
        elif len(objs_list) == 0:
            objects_str = 'nothing'

        else:
            objects_str = ', '.join(objs_list[:-1]) + ' and ' + objs_list[-1]

        text = general_desc[(self.plx, self.ply)] + ', you see ' + objects_str
        print(text)

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
            print('You are being prompted to type something')
            sleep(1)
            print('For the list of actions you can do, type "actions"')
            sleep(1)
            print()

        elif self.obj not in self.actions:
            print(f'Action "{self.obj}" not recognised')

        elif self.obj == 'walk':
            print('The walk action takes the form of "walk <direction>"')
            sleep(1)
            print('The valid directions are "up", "down", "left", and "right"')

        elif self.obj == 'grab':
            print('The grab action takes the form of "grab <object>"')
            sleep(1)
            print('The objects that are around you will be told to you')  # TODO

        elif self.obj == 'inventory':
            print('The inventory action takes the form of "inventory"')
            sleep(1)
            print('It will tell you what you have in your inventory')

        elif self.obj == 'drop':
            print('The drop action takes the form of "drop <object>"')
            sleep(1)
            print('It will drop an item from your inventory into the current area')

        elif self.obj == 'scan':
            print('The scan action takes the form of "scan"')
            sleep(1)
            print('It will inform you of your surroundings and tell you what objects are around.')

        elif self.obj == 'use':
            print('The use function takes the form of "use <item>"')
            sleep(1)
            # TODO

        elif self.obj == 'help':
            print('The help function takes the form of "help <action>"')
            sleep(1)
            print('If there is no action provided, it will tell you the general help')
            sleep(1)
            print('It will tell you how the action is used and what it does')

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
            print(f'Direction "{self.obj}" isn\'t recognised')

        else:
            dx, dy = dirs[self.obj]
            if (self.plx + dx, self.ply + dy) in map_spaces:  # if space is on the map
                if map_spaces[(self.plx + dx, self.ply + dy)] <= self.max_lvl:  # if level of space is unlocked
                    self.plx += dx
                    self.ply += dy
                    # print(f'You walked {self.obj}')

                    self.lvl = map_spaces[(self.plx, self.ply)]  # update level you are in

                    self.describe_area()
                else:
                    print('You have not unlocked this area yet')
            else:
                print('You walked into a wall')

    def grab(self):  # grab action moves object from the areas object list to players inventory
        if self.obj is None:
            print('This action is used in the form "grab <object>"')
        if self.obj in self.objects[(self.plx, self.ply)]:  # if the object is in the room
            self.objects[(self.plx, self.ply)].remove(self.obj)
            self.inventory.append(self.obj)
            print(f'You picked up the {self.obj}')
        else:  # if the object isn't there to grab.
            print(f'There isn\'t "{self.obj}" in the area')

    def drop(self):  # drop action moves object from your inventory to the areas object list
        if self.obj is None:
            print('This action is used in the form "drop <object>"')
        if self.obj in self.inventory:  # if the object is in your inventory
            self.objects[(self.plx, self.ply)].append(self.obj)
            self.inventory.remove(self.obj)
            print(f'You dropped the {self.obj}')
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
            print(', '.join(self.inventory))

    def print_actions(self):
        print('The recognised actions are:')
        print(', '.join(self.actions))

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
            print(f'Action "{self.action}" not recognised')

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
            self.response = input('>')
            self.parse_inp()


if __name__ == '__main__':
    game = Game()
    game.main()
