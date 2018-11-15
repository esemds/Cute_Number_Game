#!/usr/bin/python

import sys
import random

CRED = '\033[91m'
CEND = '\033[0m'
CYELLOW = '\033[33m'
CGREEN  = '\033[32m'
CBLUE   = '\33[34m'
#print(CYELLOW + "XXX" + CEND)

print"""
    This is a number guessing game which you enter boundries
    and try to guess a number in that range you entered.
    funny and simple. by HASAN esemds.
    remember you have only five trys.
    To start you need to enter boundries.
    """

def number_game():

    zone = str(raw_input(CBLUE+"Enter 2 integer in a-b format >> "+CEND))
    zone_main = zone.split("-")
    bound_1 = int(zone_main[0])
    bound_2 = int(zone_main[1])

    if bound_1 > bound_2:
        num_min = bound_2
        num_max = bound_1
    else:
        num_max = bound_2
        num_min = bound_1

    rand_num = random.randint(num_min, num_max)

    print(CGREEN + "Now Guess my number!!!" + CEND)

    try_time = 5

    play = 0
    while play < try_time:
        guess = int(raw_input("Enter an integer : >>"))
        if guess == rand_num:
            print(CYELLOW+"Perfect You won game."+CEND)
            play_again()

        elif guess <= rand_num: 
            print(CRED+"Try a biiger one!"+CEND)
        elif guess >= rand_num:
            print (CRED+"Try a samller one!" +CEND)

        play +=1
        if play == try_time:
            print(CRED+"You Lost Game."+CEND)
            play_again()
def play_again():
    Y_N = str(raw_input("Wanna play again? >>"))
    while True:
        try:
            if Y_N == 'y':
                number_game()
            else:
                print(CRED+"Now you are exitting The GAME!"+CEND)
                exit(1)
                #sys.exit(1)
        except ValueError:
            print(CRED + "There is an error" + CEND)
            break


number_game()