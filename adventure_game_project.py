# The goal here is to create an adventure game.
# The game gives players a description of what's happening, and then asks them to make a choice.
# Something different happens depending on the choice the player made.
# The game also includes some random factors, so that it's a little different each time.
# The game has conditions for winning and losing.
# When the game is over, it asks if the player wants to play again.

import time


armor = []


def print_pause(message):
    print(message, flush=True)
    time.sleep(0)


def play_again():
    while True:
        play_again = input(
            "Would you like to play again?\n" "Please type: Yes or No\n").lower()
        if 'yes' in play_again:
            intro()
            global armor
            armor = []
        elif 'no' in play_again:
            print_pause("Thank you for playing!")
            exit()
        else:
            print_pause("Please enter 'Yes' or 'No'\n")


def intro():
    print_pause("You find yourself in a warzone...")
    print_pause(
        "The people of Zaire are afraid of Khodos.. they say he is hiding out in a building nearby.")
    print_pause(
        "Khodos has destroyed many homes in the warzone, and some say he's made some of the folks disappear...")
    print_pause("The people of Zaire plea for your help!")
    print_pause("You do have the Sword of Dominance in your inventory!")
    print_pause("There is a building to your right.")
    print_pause(
        "To your left, there is an empty tunnel... that you are curious about...\n")
    destination()


def destination():
    while True:
        choice = input(
            "Where do you want to go?\n\n" "1. Inside the empty tunnel\n" "2. Towards the building\n")
        if choice == '1':
            tunnel()
            break
        elif choice == '2':
            building()
            break
        else:
            print_pause(
                "Sorry, I do not understand your selection.\n (Please enter 1 or 2)\n")


def tunnel():

    if 'invincible' in armor:
        print_pause(
            "The blacksmith has already equipped you with the armor!")
        print_pause("We shall see if Khodos can win the fight now...")
        print_pause("You return to the warzone of Zaire...")
        destination()
    else:
        print_pause("You walk towards the empty tunnel...")
        print_pause("The tunnel is dark, but you hear a voice..")
        print_pause("The voice tells you to come inside!")
        print_pause("There is a blacksmith waiting for you...")
        print_pause(
            "He explains that he has been waiting for a brave man to come inside the tunnel...")
        print_pause(
            "He has been hiding inside the tunnel from Khodos, while he's been hiding...")
        print_pause(
            "The blacksmith has created a special type of body armor called: invincible")
        print_pause(
            "He equips you with this armor, in order to defeat Khodos and not take any damage!")
        armor.append('invincible')
        print_pause("You return to the warzone in Zaire...")

    destination()


def building():
    print_pause("You listen to the people of Zaire!")
    print_pause("You approach the building with your Sword of Dominance..")
    print_pause("Before you get close enough to the building")
    print_pause("Khodos runs outside the building and attacks you!\n\n")
    fight_choice()


def fight_choice():
    while True:
        fight_choice = input(
            "1. Would you like to fight Kodos with your Sword of Dominance?\n" "2. Would you rather return to the warzone and re-think the situation?\n\n")
        if fight_choice == '1':
            if 'invincible' in armor:
                print_pause(
                    "You swing your Sword of Dominance at Khodos twice, dealing damage!")
                print_pause(
                    "Khodos retaliates with a very strong breath of fire that he sprays at you!")
                print_pause("The fire does zero damage...")
                print_pause(
                    "Your 'invincible' armor has blocked all incoming damage!")
                print_pause(
                    "Kodos realizes he has no other choice, but to flee the warzone!")
                print_pause(
                    "Congratulations, you are victorious! You have saved the town of Zaire from Khodos!")
                play_again()
            else:
                print_pause(
                    "You swing your Sword of Dominance at Khodos twice, dealing damage!")
                print_pause(
                    "Khodos retaliates with a very strong breath of fire that he sprays at you.")
                print_pause(
                    "Unfortunately, the fire deals 100 damage to you, and you die.")
                play_again()
        elif fight_choice == '2':
            print_pause("You run as fast as you can to avoid Khodos...")
            print_pause(
                "Khodos laughs at you... and screams 'NO ONE CAN DEFEAT ME!'")
            print_pause(
                "You return back to the town of Zaire, to re-think the situation.")
            destination()
        else:
            print_pause(
                "Sorry, I did not understand you!\n" "Please select a choice: 1 or 2\n")


def play_game():
    intro()
    destination()


play_game()
