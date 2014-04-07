#import msvcrt as m
#ch = "init"
#def wait():
#    ch=m.getch()
#    print ch

import time

while True:
    choice = raw_input("> ")

    if choice == 'b' :
        print choice
        break
    else :
        print "running"
        time.sleep(2) 
