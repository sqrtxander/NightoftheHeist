# imports
from time import sleep

# variables
inventory = ['stone']
actions = ('walk', 'grab', 'view', 'use')
objects = [['stone', 'key'],  # level 0 objects
           ['bag', 'soap']]  # level 1 objects
plx, ply = 0, 0  # player's x and y coordiates
level = 0


def help_():
    pass


def parse_inp(inp):  # TODO
    if 'help' in inp.lower():
        help_()
    elif 'inventory' in inp.lower():
        print('The items in your inventoiry are:')
        for i in inventory:
            print(i)

    inp_list = inp.lower().strip().split(' ')  # get a list of the words in the input

    try:
        action = inp_list[0]
        noun = inp_list[1]
    except IndexError:  # if there is less than 2 words in the input
        print(f'Unknown action {inp}.')
        return  # stops the rest of the function from executing

    if action not in actions:
        print(f'Unknown action {action}.')

    elif action == 'grab':  # grab action moves object from the specific levels list to players inventory
        if noun in objects[level]:
            objects[level].remove(noun)
            inventory.append(noun)

        else:  # if the object isn't recognised
            print(f'Unknown object {noun}')


if __name__ == '__main__':  # currently test code

    while True:
        response = input()
        parse_inp(response)

        print(f'inventory {inventory}')
        print(f'objects {objects[level]}')
