wrong = ("Incorrect.")
numberOnly = ("You may only type in digits.")
lockStatus = "locked"
breaker = ("\n--------------------------------------\n")


print("You notice the light on the keypad is on. Would you like to attempt the code? yes || no")
accept = raw_input("\n\nResponse: ")
print breaker
if accept == "yes":
    for code in range(3):
        digitOne = raw_input("\nFirst digit: ");
        while (digitOne.isdigit() == False):
            print numberOnly
            digitOne = raw_input("\nFirst digit: ");
        if int(digitOne) == 1:
            print ("correct")
            print breaker
            digitTwo = raw_input("\nSecond digit: ");
            while (digitTwo.isdigit() == False):
                print numberOnly
                digitTwo = raw_input("\nSecond digit: ");
            if int(digitTwo) == 2:
                print ("correct")
                print breaker
                digitThree = raw_input("\nThird digit: ");
                while (digitThree.isdigit() == False):
                    print numberOnly
                    digitThree = raw_input("\nThird digit: ");
                if int(digitThree) == 3:
                    print ("correct")
                    print breaker
                    lockStatus = "unlocked"
                    break

                else:
                    print wrong

            else:
                print wrong

        else:
            print wrong

print ("\ndoor is ") + lockStatus
