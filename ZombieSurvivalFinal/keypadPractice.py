wrong = ("Incorrect.")
numberOnly = ("You may only type in digits.")
lockStatus = "locked"
breaker = ("\n--------------------------------------\n")


print("You notice the light on the keypad is on. Would you like to attempt the code? yes || no")
accept = raw_input("\n\nResponse: ")
print breaker
if accept == "yes"


digitOne = raw_input("\nFirst digit: ");
while (digitOne.isdigit() == False):
    print numberOnly
    digitOne = raw_input("\nFirst digit: ");
if int(digitOne) == 1:
    print ("correct")
    print breaker

"""for code in range(3):
    if accept == "yes":
        digitOne = raw_input("\nFirst digit: ");
        if digitOne.isdigit() == True:
            if int(digitOne) == 1:
                print ("correct")
                print breaker


                digitTwo = raw_input("\nSecond digit: ");
                if digitTwo.isdigit() == True:
                    if int(digitTwo) == 2:
                        print ("correct")
                        print breaker


                        digitThree = raw_input("\nThird digit: ");
                        if digitThree.isdigit() == True:
                            if int(digitThree) == 3:
                                print("correct")
                                print breaker
                                lockStatus = "unlocked"
                                break;
                            else:
                                print wrong;
                                print breaker;
                        else:
                            print numberOnly;
                            print breaker;
                    else:
                        print wrong;
                        print breaker;
                else:
                    print numberOnly;
                    print breaker;
            else:
                print wrong;
                print breaker;
        else:
            print numberOnly;
            print breaker;

print ("the door is" + " " + lockStatus + "\n\n")


wrong = ("Incorrect.")
numberOnly = ("You may only type in digits.")
lockStatus = "locked"
breaker = ("\n--------------------------------------\n")


print("You notice the light on the keypad is on. Would you like to attempt the code? yes || no")
accept = raw_input("\n\nResponse: ")
print breaker
wrongAttempts = 0

if accept == "yes":
    for x in range(1, 3, 1):
        if (x == 1) and (wrongAttempts < 4):
            digitOne = raw_input("\nFirst digit: ");
            if digitOne.isdigit() == True: #checking to make sure this is a number  BUT IS USELESS WHEN YOU ENTER NEGATIVE NUMBER
                if int(digitOne) == 1:
                    print ("correct")
                    print breaker
                    x = x+1
                else:
                    print "WTF IS GOING ON??";
                    print breaker
            else:
                print "you messed up here";
                print numberOnly;
                print breaker;
                x = 1
                wrongAttempts = wrongAttempts + 1
        else:
            print "jk, you messed here";
            wrongAttempts = wrongAttempts + 1

        if (x == 2) and (wrongAttempts < 4):
            digitTwo = raw_input("\nSecond digit: ");
            if digitTwo.isdigit() == True: #checking to make sure this is a number  BUT IS USELESS WHEN YOU ENTER NEGATIVE NUMBER
                if int(digitTwo) == 2:
                    print ("correct")
                    print breaker
                    x = x+1
                else:
                    print "Oh! Here's the problem";
                    print breaker
            else:
                print "ooooohhhh, here it is";
                print numberOnly;
                print breaker;
                x=2
                wrongAttempts = wrongAttempts + 1
        else:
            print "wow, finally figured it out";
            wrongAttempts = wrongAttempts + 1

        if (x == 3) and (wrongAttempts < 4):
            digitThree = raw_input("\nThird digit: ");
            if digitThree.isdigit() == True: #checking to make sure this is a number  BUT IS USELESS WHEN YOU ENTER NEGATIVE NUMBER
                if int(digitThree) == 3:
                    print ("correct")
                    lockStatus = "unlocked"
                    print breaker
                    x = x+1
                else:
                    print "wrong";
                    print numberOnly;
                    print breaker;
                    x=3
                    wrongAttempts = wrongAttempts + 1
            else:
                print "hahahaha";
                wrongAttempts = wrongAttempts + 1
        break;

print ("the door is" + " " + lockStatus + "\n\n")
print wrongAttempts
print x
"""
