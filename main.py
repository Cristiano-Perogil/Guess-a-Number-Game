from random import randint
import sys
import time

# Generating a random number from the range the user must pass as argument before running the file
def generatingRandomNumber():
    argv1 = int(sys.argv[1])
    argv2 = int(sys.argv[2])
    number = randint(argv1, argv2)
    return gettingPlayersName(number, argv1, argv2)

# Getting the name of who will play
def gettingPlayersName(number, argv1, argv2):
    print(f"hellow!\nWelcome to our guessing a number game.\n We wonder if you will be that lucky one or if the luck has turned its back to you\nWell, let\'s find out!\nYou have to guess a number between {argv1} and {argv2}\nBefore starting:")
    # Creating a list of players (in case of more than one to play)
    players = []
    name = input("What is your name? ")
    # Appending to the list the name of the first one who inputs it (in case of only one player)
    players.append(name)
    somoneElse = input("Is there somebody else playing with you? Type Y for adding them or any other letter to move on: ")
    while somoneElse.upper() == "Y":
        playerName = input("Type here their name: ")
        players.append(playerName)
        newplayer = input("Someone else? If you type Y, we add them otherwise type any other letter and let\'s get started: ")
        # Adding as much players as is wanted to
        if newplayer.upper() == 'Y':
            continue
        # In case of more than one player, starting the multi-players version
        return guessing(number, argv1, argv2, players)
    # Otherwise, starting the single one
    return guessingSingleVersion(number, argv1, argv2, name)

'''
Creating the guessing function 
Note: it is known it would be better not using a for loop to handle the next player attempt because in case of miss-spelling it automatically moves to the next one, 
however, that what makes it harder and nicer
'''
def guessing(number, rgv1, rgv2, players):
    print(f"It seems you and your friends are trying to see who is luckier.\nWell let's get started")
    # Starting a counter variable to handle the attempts quantity
    attempts = 0
    start = True
    while start:
        for player in range(len(players)):
            print(f"It\'s your turn {players[player]} guess a number between {rgv1} and {rgv2}: ")
            try:
                guessing = int(input(""))
                if guessing < rgv1 or guessing > rgv2:
                    print(f"Be sure you enterd a number between {rgv1} and {rgv2}\nMoving on to the next one...")
                    continue
                elif guessing != number:
                    print("We are sorry, but you could not get it.")
                    # Iterating the attempts variable
                    attempts += 1
                    # calling the function that handles the attempts in case the players have tried several times
                    handlingMultipleAttempts(attempts)
                    continue
                elif guessing == number:
                    print(f"{number} waw You made it!!!!\n You should try the lottery {players[player]}!\n Thank you for using this application!\n Invite your friends to check if they are that lucky one as you are.")
                    start = False
                    break  
            except ValueError:
                print("Just numbers are allowed in a guessing number game! Moving to the next one...")
                continue

# Creating the single version
def guessingSingleVersion(number, rgv1, rgv2, name):
    print(f"Well {name}, let\'s get started...")
    while True:
        try:
            guessing = int(input("Type here your try: "))
            if guessing < rgv1 or guessing > rgv2:
                print(f"Be sure you enterd a number between {rgv1} and {rgv2}")
                continue
            elif guessing != number:
                print("We are sorry, but you could not get it. Please try again!")
                continue
            elif guessing == number:
                print(f"{number} waw You made it!!!!\n {name}, you should try the lottery!\n Thank you for using this application!\n Invite your friends to check if they are that lucky one as you are.")
                break
        except ValueError:
            print("Just Numbers are allowed in a guessing number game! ")
            continue

'''
Creating a function to handle multiple attempts
Note: The time.sleep() method is used here to hold down the script to run
as it displays a message according to how many attempts are taken.
This action is taken to ensure that a voice screen reader will read the message,
something that is not possible if the script immediately asks another prompt.
'''
def handlingMultipleAttempts(attempts):
    if attempts == 5:
        print("Well, it seems that the luck is not around, is it?")
        time.sleep(10)
    elif attempts == 10:
        print("Look, I know I should be cool, nevertheless if you guys have tried 10 times and did not catch the luck,\nWhen you finally guess the number, eit won\'t be luck anymore! ")
        time.sleep(10)
    elif attempts == 20:
        print("Seriously, you should definatly stop! LOL, I won\t be letting anyone else know anymore.")
        time.sleep(10)

if __name__ == '__main__':
    generatingRandomNumber()