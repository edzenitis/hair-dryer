"""

20140409
Test threading
20140409
Seems to work well.
This will be very useful for making a control loop that
runs along independently. 

ToDo
- Try adding the time check. The loop sleep timing is not very accurate. 

"""

# Imports and setup
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


def loop1():
    n = 1
    max_n = 20
    state = "loop" 
    while (state == "loop"):
        print "loop1 print,", n, ",", time.time()
        time.sleep(0.5)
        n = n + 1
        if (n > max_n):
            state = "end"
    # end of loop1

def loop2():
    n = 1
    max_n = 10
    state = "loop" 
    while (state == "loop"):
        print "loop2 print,", n, ",", time.time()
        time.sleep(2)
        n = n + 1
        if (n > max_n):
            state = "end"
    # end of loop2

#def keypress():
#    global char
#    char = getch()
 
thread.start_new_thread(loop1, ())
thread.start_new_thread(loop2, ())
