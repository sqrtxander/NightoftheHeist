# imports
from time import sleep


# variables
inventory = ['stone']
actions = {'walk': 0, 'grab': 0, 'view', 0}

def help_():
    pass


def parse_inp(inp):
    if 'help' in inp.lower():
        help_()
    elif 'inventory' in inp.lower():
        print('The items in your inventoiry are:')
        for i in inventory:
            print(i)

    inp_list = inp.lower().strip().split(' ') # get a list of the words in the inp
    if inp_list[0] not in actions:
        print(f'Unknown action {inp}.')




