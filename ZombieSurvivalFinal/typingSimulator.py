import sys,time,random

#mimics real person typing~
typingSpeed = 50 #wpm
def slowType(x):
    for i in x:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typingSpeed)
    print ''

slowType("I have a very strong desire to understand people and why they think and behave the way they do, so I can improve myself, borrowing their better qualities.")
