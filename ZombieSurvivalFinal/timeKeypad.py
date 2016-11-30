import sys
import time

def countdown(t): # in seconds
    for i in range(t,0,-1):
        print 'tasks done, now sleeping for %d seconds\r' % i,
        sys.stdout.flush()
        time.sleep(1)
countdown(10)
