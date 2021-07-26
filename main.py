# imports
import random
from time import sleep
from math import ceil


def intro_text():
    print('Welcome to Night of the Heist, A game by Xander')
    sleep(3)
    print('It is midnight and you are about to rob a bank')
    sleep(2)
    print('You roll up in your car and prepare to get out')
    sleep(2)
    print('At any point during the game, you can use the "help" action')
    sleep(2)
    print('Get ready')
    sleep(3)


def slow_print(text, delay):
    for char in text:
        print(char, end='')
        sleep(delay)
    print()


def replay():
    again = input('Would you like to play again? (y/n)\n')
    if again.strip().lower() in ['y', 'yes']:  # if response is yes
        return True
    elif again.strip().lower() in ['n', 'no']:  # if response is no
        print('Thanks for playing Night of the Heist')
        return False
    else:  # if response is unrecognised
        print('Your response was not recognised')
        sleep(1)
        return replay()


def get_num(text):
    while True:
        try:
            num = input(text)
            return int(num)
        except ValueError:
            print('Number must be an integer')
            continue


class Game:

    def __init__(self):  # declaring all the variables
        self.response = None
        self.action = None
        self.item = None
        self.inventory = []
        self.actions = ('help', 'inventory', 'actions', 'scan', 'walk', 'grab', 'drop', 'use', 'read', 'enter code')
        self.items = {(0, 0): ['wire', 'crowbar'], (1, 0): ['rock', 'key'],  # level 0 items
                      (1, 1): [], (1, 2): [], (1, 3): ['cloth'],  # level 1 items
                      (0, 2): ['backpack'],  # level 2 items
                      (2, 3): ['paper'], (3, 3): [],  # level 3 items
                      (3, 2): []}  # level 4 items
        self.plx, self.ply = 0, 0  # player's x and y coordinates
        self.unlocked_lvls = [True, False, False, False, False]
        self.vault_code = str(random.randint(0000, 9999)).zfill(4)  # generates a 4 digit code from 0000 to 9999
        self.turns_till_over = 50
        self.visited_vault = False
        self.score = 0

    def describe_area(self):  # describe area function prints the description of what is around you and what you see
        general_desc = {(0, 0): '''South west of bank''',
                        (1, 0): 'South of bank, there is a door above you',
                        # level 0 descriptions
                        (1, 1): 'Entrance of bank, there is a pathway above you, the door is below you',
                        (1, 2): 'Entrance of bank, there is a door that says "Authorised personnel only" on your left, '
                                'there are walkways above and below you',
                        (1, 3): 'Entrance of bank, there is a hallway to the right of you, '
                                'there is a walkway below you',
                        # level 1 descriptions
                        (0, 2): 'You are in the authorised personnel only zone, '
                                'there is a keypad with a 4 digit code entry system, the entrance is to your right',
                        # level 2 descriptions
                        (2, 3): 'You are in a narrow hallway, the entrance is to your left, '
                                'there is an opening to your right',
                        (3, 3): 'You are in a narrow hallway, you manage to make out a vault door below you, '
                                'the hallway continues to the left',
                        # level 3 descriptions
                        (3, 2): 'You are in the vault, money is scattered everywhere, the door is above you'
                        }  # level 4 descriptions

        # takes list and puts it in the form 'a 0, a 1, a 2 and a 3'
        items_list = ['a ' + i for i in self.items[(self.plx, self.ply)]]  # starts each item with the string 'a '
        if len(items_list) == 1:
            items_str = items_list[0]
        elif len(items_list) == 0:
            items_str = 'nothing'

        else:
            items_str = ', '.join(items_list[:-1]) + ' and ' + items_list[-1]

        # if player is in the vault without items around them, we don't want to say you see nothing
        if (self.plx, self.ply) == (3, 2) and not self.items[(3, 2)]:
            desc_text = general_desc[(self.plx, self.ply)]
        else:
            desc_text = general_desc[(self.plx, self.ply)] + ', you see ' + items_str

        print(desc_text)

    def help_(self):  # help function tells the user how each action works
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

        elif self.item in ('walk', 'go'):
            print('The walk action takes the form of "walk <direction>"')
            sleep(1)
            print('The valid directions are "north", "east", "south", and "west"')
            sleep(1)
            print('You can also use "up", "right", "down", and "left", or "N", "E", "S", and "W"')
            sleep(1)
            print('You are controlling your character from a birds eye point of view i.e. you are always facing North')

        elif self.item in ('grab', 'get'):
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
            print('It will inform you of your surroundings and tell you what items are around')

        elif self.item == 'use':
            print('The use action takes the form of "use <item>"')
            sleep(1)
            print('It will ask you what you want to use the item on')
            sleep(1)
            print('It allows you to complete sections of the game performing necessary actions to unlock new areas')

        elif self.item in ('enter', 'code'):
            print('The enter code action takes the form of "enter code"')
            sleep(1)
            print('You are only able to use it when you are in the authorised personnel only zone')
            sleep(1)
            print('You will be asked to enter the code or to cancel')

        elif self.item == 'read':
            print('The read action takes the form of "read <item>"')
            sleep(1)
            print('If you have the item on you it will tell you what it says')

        elif self.item == 'help':
            print('The help function takes the form of "help <action>"')
            sleep(1)
            print('If there is no action provided, it will tell you the general help')
            sleep(1)
            print('It will tell you how the action is used and what it does')

        elif self.item not in self.actions:
            print(f'Action "{self.item}" not recognised')

    def walk(self):
        map_spaces = {(0, 0): 0, (1, 0): 0,
                      (1, 1): 1, (1, 2): 1, (1, 3): 1,
                      (0, 2): 2,
                      (2, 3): 3, (3, 3): 3,
                      (3, 2): 4}

        dirs = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0),
                'up': (0, 1), 'right': (1, 0), 'down': (0, -1), 'left': (-1, 0),
                'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}

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

                    if (self.plx, self.ply) == (1, 0) and self.visited_vault:  # if you are about to win
                        return  # don't describe the area

                    self.describe_area()
                else:
                    print('You have not unlocked this area yet')
            else:
                print('You walked into a wall')

        if (self.plx, self.ply) == (3, 2):  # if player is in the vault
            if self.unlocked_lvls[0]:  # if the outside area is unlocked
                sleep(1)
                print('You hear the sound of the entrance slamming shut')
                self.unlocked_lvls[0] = False  # locks the outside area
            self.visited_vault = True

    def grab(self):  # grab action moves item from the area's item list to player's inventory capping at 5 items in
        # the player's inventory and 10 if they are holding a backpack

        if self.item is None:  # if the item to grab is not provided
            print('This action is used in the form "grab <item>"')
            return

        if 'backpack' in self.inventory:
            inv_spaces = 10 - len(self.inventory) - self.score//150000
        else:
            inv_spaces = 5 - len(self.inventory) - self.score//150000

        if inv_spaces <= 0:  # if your hands are full
            print('You are holding too many things at once')

        elif (self.plx, self.ply) == (3, 2) and self.item == 'money':  # if player is in the vault and picking up money
            print(f'You picked up ${150000 * inv_spaces}')
            self.score += 150000 * inv_spaces

        elif self.item in self.items[(self.plx, self.ply)]:  # if the item is in the room
            self.items[(self.plx, self.ply)].remove(self.item)  # removes the item from the area's item list
            self.inventory.append(self.item)  # adds the item to the player's inventory
            print(f'You picked up the {self.item}')

        else:  # if the item isn't there to grab.
            print(f'There isn\'t "{self.item}" in the area')

    def drop(self):  # drop action moves item from player's inventory to the area's item list

        if self.item is None:  # if the item to drop is not provided
            print('This action is used in the form "drop <item>"')

        elif self.item == 'money':
            amount = get_num('How much money do you want to drop? '
                             '(response will be rounded up to the nearest $150000)\n')
            amount = ceil(amount/150000) * 150000  # rounds amount up to the nearest 150000
            if self.score >= amount:
                self.score -= amount
                print(f'You dropped ${amount}')
                sleep(1)
                if (self.plx, self.ply) != (3, 2):
                    print('The money mysteriously disappears, go back to the vault to get more')
            else:
                print(f'You do not have ${amount} to drop')

        elif self.item in self.inventory:  # if the item is in your inventory
            self.items[(self.plx, self.ply)].append(self.item)  # adds the item to  the area's item list
            self.inventory.remove(self.item)  # removes the item from the player's inventory
            print(f'You dropped the {self.item}')

        else:
            print(f'There isn\'t "{self.item}" in your inventory')

    def use(self):  # use function completes actions that are required for the game to progress

        if self.item is None:
            print('This action is used in the form "use <item>"')
            return  # stops the rest of the function from executing

        if self.item not in self.inventory:  # if player does not have the item in their inventory
            print(f'You do not have a "{self.item}" to use')
            return  # stops the rest of the function from executing

        obj = input(f'What would you like to use the {self.item} on?\n').strip().lower()

        if (self.plx, self.ply) == (1, 0) and not self.visited_vault:  # if standing beneath the door to the bank
            if any(x in obj for x in ('door', 'lock')):  # if obj is door or lock
                if not self.unlocked_lvls[1]:  # if level 1 not unlocked
                    if self.item == 'wire':
                        print('You manage to pick the lock. The door creaks open')
                        self.unlocked_lvls[1] = True
                        self.unlocked_lvls[3] = True
                    elif self.item == 'crowbar':
                        print('The door doesn\'t open, these marks will surely attract the authorities')
                        self.turns_till_over -= 2
                    elif self.item == 'key':
                        print('The key doesn\'t fit the lock')
                    else:
                        print(f'You can\'t use the {self.item} on the {obj}')
                else:
                    print('You have already unlocked the door')

        elif (self.plx, self.ply) == (1, 2):  # unlocking the authorised personnel only door
            if not self.visited_vault:
                if any(x in obj for x in ('door', 'lock')):
                    if not self.unlocked_lvls[2]:
                        if self.item == 'key':
                            print('The key worked, the door is open')
                            self.unlocked_lvls[2] = True
                        elif self.item == 'crowbar':
                            print('Maybe it\'s best not to make such a loud sound. The door remains locked')
                            self.turns_till_over -= 2
                        else:
                            print(f'You can\'t use the {self.item} on the {obj}')
                    else:
                        print('You have already unlocked this area')
                else:
                    print(f'You can\'t use the {self.item} on the {obj}')
            if self.visited_vault:
                if any(x in obj for x in ('door', 'lock')):
                    if self.item == 'cloth':
                        print('You wipe your fingerprints off the keyhole')
                        self.turns_till_over += 10
                    else:
                        print(f'You can\'t use the {self.item} on the {obj}')
                else:
                    print(f'You can\'t use the {self.item} on the {obj}')
        elif (self.plx, self.ply) == (1, 1) and self.visited_vault:
            if any(x in obj for x in ('door', 'lock')):  # if obj is door or lock
                if not self.unlocked_lvls[0]:  # if level 0 not unlocked
                    if self.item == 'wire':
                        print('You manage to pick the lock. The door creaks open')
                        self.unlocked_lvls[0] = True
                    elif self.item == 'crowbar':
                        print('The door doesn\'t open, these marks will surely attract the authorities')
                        self.turns_till_over -= 2
                    elif self.item == 'key':
                        print('The key doesn\'t fit the lock')
                    else:
                        print(f'You can\'t use the {self.item} on the {obj}')
                else:
                    print('You have already unlocked the door')

        else:
            print(f'You can\'t use the {self.item} on the {obj}')

    def enter_code(self):
        if (self.plx, self.ply) == (0, 2):
            if not (self.unlocked_lvls[4] or self.visited_vault):  # if you haven't unlocked the vault yet
                code_guess = input('Enter code (or enter "cancel"): ')
                if code_guess == self.vault_code:  # if the guess is correct
                    self.unlocked_lvls[4] = True
                    print('You hear a metal swinging sound in the distance, '
                          'the words "Vault unlocked" appear on the screen')
                elif 'cancel' in code_guess:  # if the player requested to cancel
                    self.describe_area()
                else:  # if the guess is incorrect
                    print('Incorrect code, security called')
                    self.turns_till_over -= 10
            else:  # if the vault is already unlocked
                print('You have already unlocked the vault')
        else:  # if you are not at the right location
            print('You cannot enter the code here')

    def read(self):
        if self.item is None:
            print('The read action takes the form of "read <item>"')

        elif self.item not in self.inventory:
            print(f'You do not have the "{self.item}" to read')

        elif self.item == 'paper':
            print(f'You unfold the paper and see the numbers {self.vault_code}')
        else:
            print(f'You cannot read the {self.item}')

    def print_inventory(self):  # prints the player's inventory separated by commas
        if not self.inventory and self.score == 0:  # if inventory is empty
            print('There are no items in your inventory')
        else:
            if self.score == 0:
                print('The items currently in your inventory are:')
                print(', '.join(self.inventory))
            else:
                print('The items currently in your inventory are:')
                print(', '.join(self.inventory + [f'${self.score}']))

    def print_actions(self):  # prints the list of actions separated by commas
        print('The recognised actions are:')
        print(', '.join(self.actions))

    def parse_inp(self):
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

        elif self.action in ('walk', 'go'):
            self.walk()

        elif self.action in ('grab', 'get'):
            self.grab()

        elif self.action == 'use':
            self.use()

        elif any(x in self.response.lower() for x in ('code', 'enter')):  # if user wants to enter the code
            self.enter_code()

        elif self.action == 'read':
            self.read()

        else:
            print(f'Action "{self.action}" not recognised')

    def main(self):
        self.describe_area()
        while True:
            if self.turns_till_over <= 0:  # if you lost
                print('The door slams open')
                sleep(1)
                print('You hear someone scream at you to get on the ground')
                sleep(1)
                print('The authorities have caught you')
                sleep(1)
                slow_print('GAME OVER', 0.75)
                break

            elif self.visited_vault and (self.plx, self.ply) == (1, 0):  # if you have won
                print('You made it out with the money')
                sleep(1)
                print('You hop in your getaway car, smiling to yourself')
                sleep(1)
                print(f'You managed to haul a grand total of ${self.score}')
                sleep(1)
                slow_print('YOU WIN', 0.75)
                break

            self.response = input('> ')
            self.parse_inp()
            self.turns_till_over -= 1


if __name__ == '__main__':

    intro_text()
    print('================================================================')
    sleep(1)

    while True:
        game = Game()
        game.main()

        print('================================================================')
        sleep(1)
        if not replay():
            sleep(2)
            break
        print('================================================================')
        sleep(2)
