# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:31:38 2020

@author: anton
"""
import time
import random
def cuber():
    
    again =  True
    while again:
        try:
            input("Press enter to continue")
        except SyntaxError:
            pass
        numRand = random.randrange(100)
        cube = numRand**3
        print("Here is your cube: %i" %cube)
        
        solve = input("And the winner is: ")
        time.sleep(3)
        if int(solve) == numRand:
            print("You got it, it's: %i" %numRand)
        else:
            print("You dum")
        nextRound = input("Press Enter to continue, press Space to quit: ")
        if nextRound == "":
            return again
        elif nextRound == " ":
            break
        else:
            nextRound = input("Press Enter to continue, press Space to quit: ")
            