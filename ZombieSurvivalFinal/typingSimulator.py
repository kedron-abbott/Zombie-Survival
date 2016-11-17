import sys,time,random

#mimics real person typing~
def slowType(text,speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print ''

slowType("Seven actual words about what??? \"...sure\" says Dustin",25)
slowType("Seven actual words about what??? \"...sure\" says Dustin",75)
