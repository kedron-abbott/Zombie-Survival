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

def dropHealth(percent):
    global health
    global healthLoss
    percent = healthLoss
    health = health - percent
    print breaker
    print ("You lost ") + str(percent) + ('%') + (" of your health")
    print ("Current Health = ") + str(health) + ('%')
    print breaker
    if health < 1:
        print ("You have died")
        gameOver()

def kevinIntro(x):
    slowPrint("Name: Kevin",x)
    slowPrint("Age: 42",x)
    slowPrint("Occupation: Police Officer ",x)
    slowPrint("Height: 5\'10",x)
    newScene(3)
    slowPrint("Before walking in, I release the magazine of my pistol one last time to ensure all seven bullets are still in there.", 67)
    sleep(.8)
    slowPrint("...They are.",63)
    newScene(2)

def shoot():
    global shotsFired
    global ammoRemaining
    global hit
    hit = False
    shotsFired = shotsFired + 1
    if ammoRemaining < 1:
        print ("My weapon clicks but doesn't fire...I'm out of ammo.")
        dry = True
    else:
        ammoRemaining = ammoRemaining - 1
        shoot = int(random.choice(shootingAccuracy))
        if (shoot % 2 == 0):
            hit = True


#Classes:
#i wish i knew how to make these properly :( // it would probably help y'know


#Statuses
lockStatus = "locked"
markStatus = "lost"
doorStatus = "unknown"
shotsFired = 0
health = 100
hit = False
ammoRemaining = 7
dry = False
zombieStatus = "alive"
run = 0

#typing speeds
slow = 40
reg = 65
fast = 80
go = 107

#difficulty
easy = 25
medium = 15
hard = 8

easyHealthLoss = 15
medHealthLoss = 20
hardHeatlhLoss = 35

#Weapon Accuracy || odd number = miss / even number = hit
easyShot = [0,1,2,4,6,8,10,12] #87% Accuracy
medShot = [0,1,2,3,4,5,7,8,10] #66% Accuracy
hardShot = [1,2,3,4,5,6,7,8,9] #44% Accuracy

#default
difficulty = medium
healthLoss = medHealthLoss
shootingAccuracy = medShot
weapon = "gun"


#timer variables
stop = "go"
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(seconds=difficulty)
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
     |  __ \                       \ \    / /          (_)             /_ |      / _ \ .
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
                healthLoss = easyHealthLoss
                shootingAccuracy = easyShot
                print healthLoss
                print difficulty
                newScene(2)
                break

            elif mode == "HARD":
                difficulty = hard
                healthLoss = hardHeatlhLoss
                shootingAccuracy = hardShot
                print healthLoss
                print difficulty
                newScene(5)
                break

            elif mode == "MED" or "MEDIUM":
                difficulty = medium
                healthLoss = medHealthLoss
                shootingAccuracy = medShot
                print healthLoss
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
        kevinIntro(54)
        while True:
            slowPrint("There's shattered glass and tattered scrubs everywhere. It appears like people left in a hurry - but to where?", go)
            inspect = raw_input("\nAlthough this place has been abandoned for days, there's blood on that medical cart. Inspect || Continue \n\nResponse: ").upper().strip();
            print breaker
            if inspect == "INSPECT":
                slowPrint("\nSweeping my fingers across the side, it's clear that this blood is still fresh.", reg)
                print breaker
                inspect = "CONTINUE"
            elif inspect == "CONTINUE":
                slowPrint("I scan the area, and a broken light fixture catches my attention.\n", go)
                break

            else:
                print invalid()
            if inspect =="CONTINUE":
                slowPrint("I scan the area, and a broken light fixture catches my attention.\n", go)
                break
        break
    else:
        invalid();

while True:
    slowPrint("It's creaking loud and the flickering light is revealing something...it's a notice board - one of the only things that hasn't been damaged here.", go)
    inspect = raw_input("\nInspect || Continue \n\nResponse: ").upper().strip();
    print breaker;
    if inspect == "INSPECT":
        slowPrint("The map reads:",fast)
        slowPrint("\n*SANCTUARIES*", go)
        slowPrint("Reliquiae: 518 miles away", reg)
        slowPrint("Unum: 307 miles away", reg)
        slowPrint("Venturis: 100 miles away", reg)
        inspect == "CONTINUE"
        break;
    elif inspect == "CONTINUE":
        break
    else:
        invalid();


while True:
    print breaker
    if zombieStatus == "dead":
        break
    elif run > 0:
        break
    else:
        slowPrint("Turning away from the board, I feel a brush against my arm and my body tenses. It's a rotter.. ", fast)
        action = raw_input("\nShoot || Push || Run \n\nResponse: ").upper().strip();
        if action == "SHOOT":
            shoot()
            if hit == True:
                slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                zombieStatus = "dead"
                break
            if hit == False:
                slowPrint("\nI take aim, but the rotter was too fast! It knocked my arm away just as I shot, putting a hole in the ceiling.", fast)
                dropHealth(healthLoss)
                while hit == False:
                    action = raw_input("\nI can't let my guard down around these things! \nShoot || Push || Run \n\nResponse: ").upper().strip();
                    if action == "SHOOT":
                        shoot()
                        if hit == True:
                            slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                            zombieStatus = "dead"
                            break
                        if hit == False:
                            slowPrint("\nI shoot, but miss again. The rotter scratches me, and I start to bleed. I tighten the grip on my weapon.", fast)
                            dropHealth(healthLoss)
                    else:
                        break



        elif action == "PUSH":
            slowPrint("I kick it hard in the chest, giving myself just enough time to find my bearings and make my next move.", go)
            print breaker
            while zombieStatus == "alive":
                action = raw_input("\nI can't let my guard down around these things! \nShoot || Run \n\nResponse: ").upper().strip();
                if action == "SHOOT":
                    shoot()
                    if hit == True:
                        slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                        zombieStatus = "dead"
                        break
                    elif hit == False:
                        slowPrint("\nI shoot, but miss again. The rotter scratches me, and I start to bleed. I tighten the grip on my weapon.", fast)
                        dropHealth(healthLoss)
                elif action == "RUN":
                    run = 1
                    break
        elif action == "RUN":
            slowPrint("I make a dash for the door, nudging the rotter out of the way. There's no need to waste any of my bullets just yet..", go)
            slowPrint("As it circles around to grasp at me, it misses and pulls the fire alarm instead..", fast)
            slowPrint("\nHeavy lights strobe, and the deafening sound makes it hard to keep moving. I trip and look back to see the rotter approaching me as I pull shards of glass from my arm.", go)
            dropHealth(healthLoss)
            while zombieStatus == "alive":
                action = raw_input("\nI can't let my guard down around these things! \nShoot || Push || Run \n\nResponse: ").upper().strip();
                if action == "SHOOT":
                    shoot()
                    if hit == True:
                        slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                        zombieStatus = "dead"
                        break
                    elif hit == False:
                        slowPrint("\nI shoot, but miss again. The rotter scratches me, and I start to bleed. I tighten the grip on my weapon.", fast)
                        dropHealth(healthLoss)
                elif action == "PUSH":
                    slowPrint("I kick it hard in the chest, giving myself just enough time to find my bearings and make my next move.", go)
                    while zombieStatus == "alive":
                        action = raw_input("\nI can't let my guard down around these things! \nShoot || Run \n\nResponse: ").upper().strip();
                        if action == "SHOOT":
                            shoot()
                            if hit == True:
                                slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                                zombieStatus = "dead"
                                break
                            elif hit == False:
                                slowPrint("\nI shoot, but miss again. The rotter scratches me, and I start to bleed. I tighten the grip on my weapon.", fast)
                                dropHealth(healthLoss)
                        elif action == "RUN":
                            break

                elif action == "RUN":
                    slowPrint("I manage to get myself up before the rotter can get a hold of me.", go)
                    break


            break
        else:
            invalid();
slowPrint("I begin to hear the snarls of several rotters around the corner; no telling how many there could be.", go)
print breaker
slowPrint("Sound attracts them..", slow)
newScene(1)
slowPrint("On the wall, a little further up, I see a fire axe in its glass casing.", fast)
print "\n\nIN CASE OF EMERGENCY"
print """

    /'-./\_
   :    ||,>
    \.-'||
        ||
        ||
        ||
        """
print "   BREAK GLASS\n\n"
slowPrint("I could definitely use that in a situation like this, I don't need the extra attention. But I'd have to leave my gun..", fast)

while True:
    weaponChoice = raw_input("\nTake Axe || Keep Gun \n\nResponse: ").upper().strip();
    if weaponChoice == "TAKE AXE" or "AXE":
        slowPrint("This'll definitely come in handy. I can't waste any ammo, and I won't have to make any noise either.", go)
        weapon = "axe"
        break
    elif weaponChoice == "KEEP GUN" or "GUN":
        slowPrint("There's no way I can give up the security of this thing - it's gotten me out of some sticky situations. \nBut I'm low on ammo -  I need to make every shot count.")
        break
    else:
        invalid()

if zombieStatus == "alive":
    slowPrint("Time to finish this guy off",fast)
    while zombieStatus != "dead":
        killZombie = ("\nKill Zombie \n\nResponse: ").upper().strip();
        if killZombie == "KILL ZOMBIE" or "KILL":
            if weapon == "axe":
                slowPrint("I wait for the rotter to get just close enough before swinging the axe right into its forehead.", go)
                zombieStatus = "dead"
                break
            else:
                shoot()
                if hit == True:
                    slowPrint("\nI take aim, and send one flying right between the eyes - clean shot; that's the only way to bring them down.", fast)
                    zombieStatus = "dead"
                    print str(ammoRemaining) + " bullets left.. I've got to be more careful."
                    break
                if hit == False:
                    slowPrint("\nI take aim, but the rotter was too fast! It knocked my arm away just as I shot, putting a hole in the ceiling.", fast)
                    dropHealth(healthLoss)
newScene(1)
slowPrint("I still hear them around the corner. For my own safety, I just need to focus on getting out of h--\n", go)
slowPrint("\"HELP!!! SOMEONE PLEASE HELP! Get back..GET BACK!\"", reg)
slowPrint("\n\nI check out the sound. There's a man in scrubs weidling an arm leg, surrounded by 4 rotters.", go)
while True:
    slowPrint("\nAlthough it is my fault he's in this mess - and he's clearly struggling - he's keeping the horde busy, making it easy for me to slip out.", fast)
    saveMark = ("\nRescue || Escape \n\nResponse: ").upper().strip();
    if saveMark == "RESCUE":
        slowPrint("It's the right thing to do. I need to help him!", go)
        action = raw_input("\nDistract || Attack \n\nResponse: ").upper().strip();
        
    elif saveMark == "ESCPAE":
        slowPrint("He should have been more prepared, especially in times like this.", go)
        slowPrint("\nI need to worry about myself..", reg)
    else:
        invalid()
