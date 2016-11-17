import sys,time,random

#mimics real person typing~
def slowType(text,speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print ''

slowType("The quick brown fox jumped over the lazy river",25)
slowType("The quick brown fox jumped over the lazy river",75)
