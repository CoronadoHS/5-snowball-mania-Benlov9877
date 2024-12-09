''' 
    Name: Snowball-Mania
    Author: Benjamin Lovato
    Date: 12/3/2024
    Class: AP Computer Science Principles
    Python: 3.11.5 
'''
import random
import time

def main():
    # the main runner of the game
	# welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name = input("What is your name? ")
    opponent = input("Great to have you here, " + name + "! who would you like to play against? ")
    print(name + " vs. " + opponent)

    players = []
    players.append(name)
    players.append(opponent) 
    #print(players)
    nextPlayer = ""
    while (nextPlayer != "DONE"):
        nextPlayer = input("Are there an more opponents? If so, type them one at a time (or DONE) and press enter ")
        players.append(nextPlayer)
    players.remove("DONE")

    choice = input("Do you want to choose who you throw the snowball at or do you want it to be random? (Type Yes or No) ")

    gameplay(name, players, choice)

    


def gameplay(name, players, manual):
    while(len(players) > 1):
        thrower = random.choice(players)
        if (thrower == name):
            if(manual == "Yes"): #manual mode
                print(players)
                target = input("You are up ! Who do you want to throw a snowball at? ")
            else:    #auto mode
                #print(thrower)
                target = random.choice(players) 
                while (target == thrower):
                    target = random.choice(players)
                    #print(target)
        else:    #if thrower is not us
                #print(thrower)
                target = random.choice(players) 
                while (target == thrower):
                    target = random.choice(players)
                    #print(target)
        print(thrower + " is throwing a snowball at " + target + "!")
        hitNum = random.randint(1,5)
        sucsess = hitResult(hitNum)
        time.sleep(2)
        if (sucsess == True):
            deadNum = random.randint(1,3)
            if(deadNum == 2):
                print("It's a hit! " + target + " is down")
                players.remove(target)
            else:
                print("They have been hit but not knocked out")
        else:
            print(target + " thinks " + thrower + " can't throw")
    print(players[0] + " is the best snowballer in all the land!!!")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum == 3): # 1 in 5 chance Ryker chose 3
       if(True):
        
        return True
    return False


main()
