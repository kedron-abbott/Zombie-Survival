import random

health = 100

chance = [1,3,5,7,8,9,10]
def dropHealth(percent):
    global health
    health = health - percent
    print('\n-----------------------------------------\n')
    print ("You lost ") + str(percent) + ('%') + (" of your health")
    print ("Health = ") + str(health) + ('%')
    print('\n-----------------------------------------\n')



def attack():
    shot = int(random.choice(chance))
    if (shot % 2 == 1):
        print ("you hit")
    else:
        print ("you missed and a zombie hit you")
        dropHealth(20)


print ("fight zombie")



while health > 0:
    attack()
print ("You died")
