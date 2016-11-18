#Imports
import os
import sys
import random
import textwrap
import datetime, time
from time import sleep

#Easy Repeatables
breaker = ("\n--------------------------------------\n")
wrong = ("Incorrect.")


#Functions:
def gameOver():
    print ("\n\nGame Over\n\n")
    sys.exit()

def invalid():
    print ("Invalid response. Please try again..")
    print breaker

def clear():
    os.system("clear")

def newScene(x):
    sleep(x)
    clear()

def slowPrint(text,speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print ''

def loadingAnimation(cycles):
    clear()
    for loop in range(cycles):
        print("loading.")
        newScene(.5)
        print("loading..")
        newScene(.5)
        print("loading...")
        newScene(.5)


#Classes:
#i wish i knew how to make these properly :( // it would probably help y'know


#Statuses
lockStatus = "locked"
markStatus = "lost"

doorStatus = "unknown"

#typing speeds
slow = 40
reg = 65
fast = 80

#difficulty
easy = 25
medium = 15
hard = 8
#default
difficulty = medium

stop = "go"
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=difficulty)


#Weapon Accuracy || odd number = miss / even number = hit
CloseBatAccuracy = [0,1,2,4,6,8,10] #86% Accuracy
CloseHuntingAccuracy = [1,2,3,4,5,6,7,8,9] #44% Accuracy
CloseRevolverAccuracy = [1,2,3,4,6,8] #80% Accuracy

FarBatAccuracy = [1] #0% Accuracy
FarHuntingAccuracy = [0,1,2,4,6,8,10] #86% Accuracy
FarRevolverAccuracy = [1,2,3,4,5] #40% Accuracy

#Easy Access
    # closeShot = int(random.choice(closerange));
    # longShot = int(random.choice(longrange));
    # while True:
    # .upper().strip();

# if (num % 2 == 0): ~ even
# else: ~ odd


#Start Screen

while True:
    print ("\nWelcome to Kedron's Zombie Survival Game.")
    print('''

      _____                        __      __           _               __        ___
     |  __ \                       \ \    / /          (_)             /_ |      / _ \
     | |  | | ___ _ __ ___   ___    \ \  / /__ _ __ ___ _  ___  _ __    | |     | | | |
     | |  | |/ _ \ '_ ` _ \ / _ \    \ \/ / _ \ '__/ __| |/ _ \| '_ \   | |     | | | |
     | |__| |  __/ | | | | | (_) |    \  /  __/ |  \__ \ | (_) | | | |  | |  _  | |_| |
     |_____/ \___|_| |_| |_|\___/      \/ \___|_|  |___/_|\___/|_| |_|  |_| (_)  \___/
    ''')
    start = raw_input("\nHow would you like to start? Begin || Rules || Mode \n\nResponse: ").upper().strip()
    print breaker
    if start == "RULES":
        while True:
            begin = raw_input("Every decision and action can result in the game changing....and your time is limited. \nThe choices you make determine your fate.  \n\nAre you ready to begin? yes || no\n\nResponse: ").upper().strip()
            print breaker
            if begin == "YES":
                start = "BEGIN";
                clear();
                break
            elif begin == "NO":
                print ("Okay...just start the game up when you're ready.\n\n");
                gameOver()
                break
            else:
                invalid()
    elif start == "MODE":
        clear()
        print ("Please choose your difficulty. Easy | Medium | Hard")
        while True:
            mode = raw_input("\nResponse: ").upper().strip()
            if mode == "EASY":
                difficulty = easy
                print difficulty
                newScene(2)
                break

            elif mode == "HARD":
                difficulty = hard
                print difficulty
                newScene(5)
                break

            elif mode == "MED" or "MEDIUM":
                difficulty = medium
                print difficulty
                newScene(3)
                break

            else:
                invalid()


    elif start == "STATS":
        print ("****all this info is inaccurate for current update***")
        print ("Bat Accuracy: [80% Close Range; 0% Far Range]")
        print ("Hunting Rifle Accuracy: [44% Close Range; 86% Far Range]")
        print ("Revolver Accuracy: [80% Close Range; 40% Far Range]")
        while True:
            understood = raw_input("\nReady to start? yes || no\n\nResponse: ").upper().strip()
            if understood == "YES":
                print breaker
                start="BEGIN";
                clear();
                break
            elif begin == "NO":
                print ("Okay...just start the game up when you're ready.\n\n");
                sys.exit()
                break
            else:
                invalid()
#Beginning of Actual Game Starts Here
    elif start == "BEGIN":
        loadingAnimation(3)
        while True:
            print("You wake up, and realize that you\'ve crashed your car.\nYou\'re in an unfimiliar area, and notice how abandoned it seems. \nYou muster the strength to get out of your car and notice the searing pain\nin your head and your side as you walk toward your trunk.\nInside you see a few of your weapons.")
            weapon = raw_input("\nWhich one do you take with you? Bat || Hunting Rifle || Revolver \n\nResponse: ").upper().strip();
            print breaker
            break
        break
    else:
        invalid();

while True:
    print ("You hold the %s at your side as you scan the area.\nYou notice a run down medical center to your right and a boarded up gun shop.\nYou're badly wounded, but your %s might not be enough to face the dangers to come." %(weapon,weapon))
    area = raw_input("\nWhere do you want to go? Hospital || Gun Shop \n\nResponse: ").upper().strip();
    print breaker;
    if area == "HOSPITAL":
        while True:
            print("As you walk along through the halls, you can clearly see the hospital has been trashed in some kind of scuffle.\nYou begin to wonder what might have happened here. Suddenly you hear a noise behind the door next to you.");
            reaction = raw_input("How do you react? Ignore || Check it out || Run away \n\nResponse: ").upper().strip();
            print breaker
            if reaction == "IGNORE":
                print("You choose to ignore the sound and continue walking down the hall.\nThe idea of what could\'ve been behind that door singes your mind, but you manage to shake off the thought.\n");
                break
            elif reaction == "CHECK IT OUT":
                print("You decide you want investigate the mysterious noise. As you approach the door, you tighten the grip you have on your %s" %weapon);
                print("\nAs you slowly open the door, you ease yourself into the room. It\'s dark, and as you take a few steps into the room, the noise grows louder.")
                print("\nYou look to your left to discover a man fastening a tourniquet around his right leg, and you can't help but wince.")
                print("\n\n\"Are...are you alive?\" the man asks. You tentatively nod your head yes.") #FINISH THIS PART
                break
            elif reaction == "RUN AWAY":
                print("ran away"); #FINISH THIS PART
                break;
            else:
                invalid()
        break;
    else:
        invalid();

while True:
    print breaker
    print ("Turning the corner, you see a woman at the far end of the hall.\nShe\'s being attacked, grappling with someone around the corner who is clearly overpowering her.");
    assist = raw_input("What do you want to do? Assist || Run away \n\nResponse: ").upper().strip();
    if assist == "ASSIST":
        print("You start to approach them, and pick up speed as the woman struggles and lets out a blood-curdling scream.");
        print("\nYou yell out, \"HEY! Get off of her!\" but it\'s too late.\nThe woman is lying in a pool of red and the attacker holds her intestines by its teeth.\nSuddenly the attacker looks up and starts to crawl over her body towards you and sprints!")
        print("\nYou have little time to decide what to do; before you even know it, your %s is raised to attack." % weapon)
        break
    elif assist == "RUN AWAY":
        print("you punk"); #FINISH THIS PART
        break
    else:
        invalid();
if (closeShot % 2 == 0):
    print breaker
    if closerange == CloseBatAccuracy:
        print("You bash the moster in the side, and it goes down hard.")
        print breaker
    else:
        print ("You shoot the monster in the torso, and it files back and hits the floor hard.");
        print breaker

else:
    print breaker
    print("You missed! The attacker was too fast for you, and you find yourself with the monster on top of you.\nYou struggle to break free, but the monster is much too strong and your %s has slid out of your hand.\nThe beast rips into your neck, feasting on your tendons, and you realise there is nothing you can do." %weapon);
    gameOver()

for response in range (100):
    print("You take a brief moment to try and process what just happened, but before you can exhale, the monster is back on its feet.")
    reaction2 = raw_input("How do you react? Attack || Run Away \n\nResponse: ").upper().strip();
    if reaction2 == "ATTACK":
        print breaker
        print ("You attack again, but this time you aim for the head...")
        if (closeShot2 % 2 == 0):
            if closerange == CloseBatAccuracy:
                print("You focus all your strength into smashing the monster\'s skull. You hear a heavy crack, and the monster goes down.");
                print breaker
                break;
            else:
                print("You manage to get a successful headshot. The beast goes down.\n")
            break
        else:
            print breaker
            print("You missed! The attacker was too fast for you, and you find yourself with the monster on top of you.\nYou struggle to break free, but the monster is much too strong for you and your %s has slid out of your hand.\nThe beast rips into your neck with its teeth, feasting on your tendons, and you realise there is nothing you can do.");
            gameOver()
    break;
else:
    invalid();
