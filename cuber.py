# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:31:38 2020

@author: anton
"This program is meant to help practicing solving cubic roots. The random fucntion inputs a number from 0 to 100, and outputs its cube. 
It then waits for your solution(cubic root of the output) and evaluates it against the number that was cubed, telling you whether your solution was correct"

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
        time.sleep(2)
        if int(solve) == numRand:
            print("You got it, it's: %i" %numRand)
        else:
            print("You dum")
        #This section needs work for better input handling
        nextRound = input("Press Enter to continue, press Space to quit: ")
        if nextRound == "":
            return again
        elif nextRound == " ":
            break
        else:
            nextRound = input("Press Enter to continue, press Space to quit: ")
            
