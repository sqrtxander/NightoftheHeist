# imports
from time import sleep

# variables
inventory = ['rock']
actions = ('walk', 'grab', 'view', 'use')
objects = [['rock', 'key'],  # level 0 objects
           ['bag', 'soap']]  # level 1 objects
plx, ply = 0, 0  # player's x and y coordinates
level = 0


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


def verbs():
    print('The recognised verbs are:')
    for i in actions:
        print(i)


def rules():
    print('Here are the rules')  # TODO


def parse_inp(inp):  # TODO
    if 'help' in inp.lower():
        help_()
    elif 'inventory' in inp.lower():
        print('The items in your inventory are:')
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


def main():
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
    print('''For the rules of the game, enter the phrase "rules", 
otherwise, if you know what you're doing, press enter.''')

    response = input('>')
    if 'rules' in response.lower():
        rules()


if __name__ == '__main__':  # currently test code

    main()

    while True:
        response = input()
        parse_inp(response)

        print(f'inventory {inventory}')
        print(f'objects {objects[level]}')
