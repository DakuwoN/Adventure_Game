# This imports time module so we can use print_pause with the
# delay between print statements.

from secrets import choice
import time
# This imports the random function so the game changes each time.
import random
from urllib import response


# These are variable assignments that enable me to use the random module.
weapons = ["Sword of Dominance", "Ultimate Blade", "Dragon Blade"]
the_weapons = random.choice(weapons)

enemy = ["Khodos", "Zeus", "Rufus"]
the_enemies = random.choice(enemy)

warzone = ["Zaire", "Magic City", "Death Town"]
the_warzone = random.choice(warzone)

armor = []  # Empty list used to store the appended armor


# def typewriter_simulator(message):
#     for char in message:
#         print(char, end='')
#         if char in string.punctuation:
#             time.sleep(.5)
#         time.sleep(.03)
#     print('')


# This function creates the delay of 2 seconds between print statements.

# def print_pause(message, delay=1):
#     typewriter_simulator(message)
#     time.sleep(delay)

def print_pause(message):
    print(message, flush=True)
    time.sleep(0)


""" This function validates input for the destination of the player! """


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'The option "{option}" is invalid. Try again!')


def intro():  # This function contains the game introduction message.
    print_pause("You find yourself in a warzone...")
    print_pause(f"The people of {the_warzone} are "
                f"afraid of {the_enemies}... they say "
                "he is hiding out in a "
                "building nearby.")
    print_pause(
        f"{the_enemies} has destroyed many "
        "homes in the warzone, and "
        "some say he's made "
        "some of the folks disappear...")
    print_pause(f"The people of {the_warzone} plea for your help!")
    print_pause(f"You do have the {the_weapons} in your inventory!")
    print_pause("There is a building to your right.")
    print_pause(
        "To your left, there is an empty "
        "tunnel... that you are curious about...\n")


def destination():

    choice = valid_input(
        "Where do you want to go?\n\n"
        "1. Inside the empty tunnel\n"
        "2. Towards the building\n", ['1', '2'])
    if choice == '1':
        tunnel()
    else:
        building()


""" This is not working... Yes or No just loops"""


def play_again():

    choice = valid_input(
        "Would you like to play again?\nYes or No\n",  ['Yes', 'No']).lower()
    if choice == 'Yes':
        global the_weapons
        the_weapons = random.choice(weapons)
        global the_enemies
        the_enemies = random.choice(enemy)
        global the_warzone
        the_warzone = random.choice(warzone)
        global armor
        armor = []
        intro()
    else:
        print_pause("Thank you for playing!")
        exit()


# This function is responsible for the possible outcomes and things
#  that can happen if they decide to enter the the tunnel.
def tunnel():

    if 'invincible' in armor:
        print_pause(
            "The blacksmith has already equipped you with the armor!")
        print_pause(f"We shall see if {the_enemies} can win the fight now...")
        print_pause(f"You return to the warzone of {the_warzone}...")
        destination()
    else:
        print_pause("You walk towards the empty tunnel...")
        print_pause("The tunnel is dark, but you hear a voice..")
        print_pause("The voice tells you to come inside!")
        print_pause("There is a blacksmith waiting for you...")
        print_pause(
            "He explains that he has been "
            "waiting for a brave man to come "
            "inside the tunnel...")
        print_pause(
            "He has been hiding inside the "
            f"tunnel from {the_enemies}, while he's "
            "been hiding...")
        print_pause(
            "The blacksmith has created a "
            "special type of body armor "
            "called: invincible")
        print_pause(
            "He equips you with this armor, "
            f"in order to defeat {the_enemies} and "
            "not take any damage!")
        armor.append('invincible')
        print_pause(f"You return to {the_warzone}...")

    destination()

# This function is responsible for the actions and consequences of selecting
# the building option. This function also calls the fight_choice() function
# in it's final step.


def building():
    print_pause(f"You listen to the people of {the_warzone}!")
    print_pause(f"You approach the building with your {the_weapons}..")
    print_pause("Before you get close enough to the building")
    print_pause(
        f"{the_enemies} runs outside the building and attacks you!\n\n")
    fight_choice()


# This function asks the player if they would like to fight, followed along with
# the consequences of fighting.
def fight_choice():

    choice = valid_input(
        f"1. Would you like to fight {the_enemies} "
        f"with your {the_weapons}?\n"
        "2. Would you rather return to "
        f"{the_warzone} and re-think the "
        "situation?\n\n", ['1', '2'])
    if choice == '1':
        if 'invincible' in armor:
            print_pause(
                "You swing your Sword of "
                f"Dominance at {the_enemies} twice, "
                "dealing damage!")
            print_pause(
                f"{the_enemies} retaliates with a "
                "very strong breath of fire "
                "that he sprays at you!")
            print_pause("The fire does zero damage...")
            print_pause(
                "Your 'invincible' armor has blocked all incoming damage!")
            print_pause(
                "Kodos realizes he has no "
                "other choice, but to flee "
                f"{the_warzone}!")
            print_pause(
                "Congratulations, you "
                "are victorious! You have "
                f"saved {the_warzone} from "
                f"{the_enemies}!")

            play_again()
        else:
            print_pause(
                "You swing your Sword of "
                f"Dominance at {the_enemies} twice, "
                "dealing damage!")
            print_pause(
                f"{the_enemies} retaliates with "
                "a very strong breath of "
                "fire that he sprays at you.")
            print_pause(
                "Unfortunately, the fire deals "
                "100 damage to you, and "
                "you die.")
            play_again()
    elif choice == '2':
        print_pause(
            f"You run as fast as you can to avoid {the_enemies}...")
        print_pause(
            f"{the_enemies} laughs at you... "
            "and screams 'NO ONE CAN DEFEAT ME!'")
        print_pause("You return back to the town "
                    f"of {the_warzone} to re-think "
                    "the situation.")
        destination()
    else:
        print_pause(
            "Sorry, I did not understand "
            "you!\n" "Please select a choice: 1 "
            "or 2\n")

# This function starts the game and steps through two more functions
# the first introduction and destination.


def play_game():
    intro()
    destination()


# This function call starts the game.
play_game()
