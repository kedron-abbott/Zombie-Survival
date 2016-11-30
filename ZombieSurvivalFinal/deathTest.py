import random

health = 100
def dropHealth(percent):
    global health
    health = health - percent
    print('\n-----------------------------------------\n')
    print ("You lost ") + str(percent) + ('%') + (" of your health")
    print ("Health = ") + str(health) + ('%')
    print('\n-----------------------------------------\n')

#start "Game"
while health > 0:
    name = raw_input("what's your name: ")
    if name == "k":
        die = raw_input("will you die? ")
        health = 0
        if die == "y":
            print ("why you always lyin..")

print ("but did you really die?")
