# -*- coding: utf-8 -*-
"""
Created on Sun Apr 06 20:08:14 2014

@author: jdzenit
"""

# Imports and setup
import u6
d = u6.U6()

import time
import thread
# Parameters


# Initialization 


#state = "loop" 

# Main loop
#while(state = loop):
#    print(time.time())
#    
#print ("done")


try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
 
char = ""
 
def keypress():
    global char
    char = getch()
 
thread.start_new_thread(keypress, ())
 
while True:
    if (char == "x"):
        print "Key pressed is " + char
        break
    print "Program is running " + char
    time.sleep(2)
