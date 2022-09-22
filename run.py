
#include <stdio.h>
import random
import string

gamestate = 1
print("Welcome to Battleship Game!\n")

dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
}

print("\n-- STEP1: Creating Board --\n")
w = int(input("Enter board width (max 12): "))+1
w = int(input("Enter board height (max 12): "))+1
letterLeftBorder = 1
letterRightBorder = w-1
numberUpBorder = 1
numberDownBorder = h-1

while( w > 13 or w < 1 or h > 13 or h< 1):
    print("\nMax Height and Width are 12, please retry...")
    w = int(input("Enter board width (max 12): "))+1
    w = int(input("Enter board height (max 12): "))+1
    letterLeftBorder = 1
    letterRightBorder = w-1
    numberUpBorder = 1
    numberDownBorder = h-1