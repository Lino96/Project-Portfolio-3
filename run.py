

include <stdio.h>
import random
import string

gamestate = 1
print("Welcome to BattleShip Game!\n")

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
h = int(input("Enter board height (max 12): "))+1
letterLeftBorder = 1
letterRightBorder = w-1
numberUpBorder = 1
numberDownBorder = h-1

while( w > 13 or w < 1 or h > 13 or h< 1):
    print("\nMax Height and Width are 12, pls retry..")
    w = int(input("Enter board width (max 12): "))+1
    h = int(input("Enter board height (max 12): "))+1
    letterLeftBorder = 1
    letterRightBorder = w-1
    numberUpBorder = 1
    numberDownBorder = h-1


#FILLING MATRIX
userMatrix = [["0" for x in range(w)] for y in range(h)]
userHitMatrix = [["0" for x in range(w)] for y in range(h)]
userDamagedMatrix = [["0" for x in range(w)] for y in range(h)]
cpuMatrix = [["0" for x in range(w)] for y in range(h)]
cpuHitMatrix = [["0" for x in range(w)] for y in range(h)]
cpuDamagedMatrix = [["0" for x in range(w)] for y in range(h)]


k=0
for i in range(w):
    userMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    userMatrix[0][j]=chr(kk+64)
    kk+=1

k=0
for i in range(w):
    userHitMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    userHitMatrix[0][j]=chr(kk+64)
    kk+=1

k=0
for i in range(w):
    userDamagedMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    userDamagedMatrix[0][j]=chr(kk+64)
    kk+=1

k=0
for i in range(w):
    cpuMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    cpuMatrix[0][j]=chr(kk+64)
    kk+=1

k=0
for i in range(w):
    cpuHitMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    cpuHitMatrix[0][j]=chr(kk+64)
    kk+=1

k=0
for i in range(w):
    cpuDamagedMatrix[i][0]=k
    k+=1
kk=0
for j in range(h):
    cpuDamagedMatrix[0][j]=chr(kk+64)
    kk+=1

print("\n- Your Matrix is generated -")
for s in userMatrix:
    print(*s)

print("\n-- STEP2: Placing Ships --\n")

#2-BLOCK SHIP PLACEMENT###
#PLAYER
print("Current Ship: |x||x|")
orientation = input("Press V (vertical, up->down) o H (horizontal, left->right) to orient the 2-blocks ship\n")

while(orientation != 'V' and orientation != 'H'):
    orientation = input("Press V (vertical, up->down) o H (horizontal, left->right) to orient the 2-blocks ship\n")

if(orientation == 'V'):#VERTICAL
    print("Current Ship:")
    print("|x|")
    print("|x|")

    letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
    numberPlace = int(input("\nInsert target number:\n"))

    while(letterPlace > letterRightBorder or letterPlace < letterLeftBorder or
    numberPlace > numberDownBorder -1 or numberPlace < numberUpBorder or
    userMatrix[numberPlace][letterPlace] == 'x' or userMatrix[numberPlace+1][letterPlace] == 'x'):
        print("Ship can't  be placed out of border or over other ships, pls replace it..\n")
        letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
        numberPlace = int(input("\nInsert target number:\n"))

    userMatrix[numberPlace][letterPlace] = 'x'
    userMatrix[numberPlace+1][letterPlace] = 'x'

if(orientation == 'H'):#HORIZONTAL
    print("Current Ship:")
    print("|x||x|")

    letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
    numberPlace = int(input("\nInsert target number:\n"))

    while(letterPlace > letterRightBorder -1 or letterPlace < letterLeftBorder or
    numberPlace > numberDownBorder or numberPlace < numberUpBorder or
    userMatrix[numberPlace][letterPlace] == 'x' or userMatrix[numberPlace][letterPlace+1] == 'x'):
        print("Ship can't  be placed out of border or over other ships, pls replace it..\n")
        letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
        numberPlace = int(input("\nInsert target number:\n"))

    userMatrix[numberPlace][letterPlace] = 'x'
    userMatrix[numberPlace][letterPlace+1] = 'x'
print("\n")


#CPU
randOrientation = random.randint(0,1)#0 -> Vertical, 1 -> Horizontal

if(randOrientation == 0):#Vertical
    letterPlace= random.randint(letterLeftBorder,letterRightBorder)
    numberPlace = random.randint(numberUpBorder,numberDownBorder-1)
    print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    while(cpuMatrix[numberPlace][letterPlace] == 'x' or cpuMatrix[numberPlace+1][letterPlace] == 'x'):
        print("cpu placed WRONG")

        letterPlace= random.randint(letterLeftBorder,letterRightBorder)
        numberPlace = random.randint(numberUpBorder,numberDownBorder-1)
        print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    cpuMatrix[numberPlace][letterPlace] = 'x'
    cpuMatrix[numberPlace+1][letterPlace] = 'x'

if(randOrientation == 1):#Horizontal
    letterPlace= random.randint(letterLeftBorder,letterRightBorder-1)
    numberPlace = random.randint(numberUpBorder,numberDownBorder)
    print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    while(cpuMatrix[numberPlace][letterPlace] == 'x' or cpuMatrix[numberPlace][letterPlace+1] == 'x'):
        print("cpu placed WRONG")

        letterPlace= random.randint(letterLeftBorder,letterRightBorder-1)
        numberPlace = random.randint(numberUpBorder,numberDownBorder)
        print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    cpuMatrix[numberPlace][letterPlace] = 'x'
    cpuMatrix[numberPlace][letterPlace+1] = 'x'

print("\n")
print("-- User Matrix --")
for s in userMatrix:
    print(*s)

print("\n")
print("-- Cpu Matrix (VISIBILE ONLY IN DEBUG) --")
for s in cpuMatrix:
    print(*s)
#2-BLOCK SHIP PLACEMENT###



#3-BLOCK SHIP PLACEMENT###
#PLAYER
print("Current Ship: |x||x||x|")
orientation = input("Press V (vertical, up->down) o H (horizontal, left->right) to orient the 3-blocks ship\n")

while(orientation != 'V' and orientation != 'H'):
    orientation = input("Press V (vertical, up->down) o H (horizontal, left->right) to orient the 3-blocks ship\n")

if(orientation == 'V'):#VERTICAL
    print("Current Ship:")
    print("|x|")
    print("|x|")
    print("|x|")

    letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
    numberPlace = int(input("\nInsert target number:\n"))

    while(letterPlace > letterRightBorder or letterPlace < letterLeftBorder or
    numberPlace > numberDownBorder -2 or numberPlace < numberUpBorder or
    userMatrix[numberPlace][letterPlace] == 'x'
    or userMatrix[numberPlace+1][letterPlace] == 'x'
    or userMatrix[numberPlace+2][letterPlace] == 'x'):
        print("Ship can't  be placed out of border or over other ships, pls replace it..\n")
        letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
        numberPlace = int(input("\nInsert target number:\n"))

    userMatrix[numberPlace][letterPlace] = 'x'
    userMatrix[numberPlace+1][letterPlace] = 'x'
    userMatrix[numberPlace+2][letterPlace] = 'x'

if(orientation == 'H'):#HORIZONTAL
    print("Current Ship:")
    print("|x||x||x|")

    letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
    numberPlace = int(input("\nInsert target number:\n"))

    while(letterPlace > letterRightBorder -2 or letterPlace < letterLeftBorder or
    numberPlace > numberDownBorder or numberPlace < numberUpBorder or
    userMatrix[numberPlace][letterPlace] == 'x'
    or userMatrix[numberPlace][letterPlace+1] == 'x'
    or userMatrix[numberPlace][letterPlace+2] == 'x'):
        print("Ship can't  be placed out of border or over other ships, pls replace it..\n")
        letterPlace= dict[input("\nInsert target letter CAPITAL:\n")]
        numberPlace = int(input("\nInsert target number:\n"))

    userMatrix[numberPlace][letterPlace] = 'x'
    userMatrix[numberPlace][letterPlace+1] = 'x'
    userMatrix[numberPlace][letterPlace+2] = 'x'

print("\n")


#CPU
randOrientation = random.randint(0,1)#0 -> Vertical, 1 -> Horizontal

if(randOrientation == 0):#Vertical
    letterPlace= random.randint(letterLeftBorder,letterRightBorder)
    numberPlace = random.randint(numberUpBorder,numberDownBorder-2)
    print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    while(cpuMatrix[numberPlace][letterPlace] == 'x'
    or cpuMatrix[numberPlace+1][letterPlace] == 'x'
    or cpuMatrix[numberPlace+2][letterPlace] == 'x'):
        print("cpu placed WRONG")

        letterPlace= random.randint(letterLeftBorder,letterRightBorder)
        numberPlace = random.randint(numberUpBorder,numberDownBorder-2)
        print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    cpuMatrix[numberPlace][letterPlace] = 'x'
    cpuMatrix[numberPlace+1][letterPlace] = 'x'
    cpuMatrix[numberPlace+2][letterPlace] = 'x'

if(randOrientation == 1):#Horizontal
    letterPlace= random.randint(letterLeftBorder,letterRightBorder-2)
    numberPlace = random.randint(numberUpBorder,numberDownBorder)
    print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    while(cpuMatrix[numberPlace][letterPlace] == 'x'
    or cpuMatrix[numberPlace][letterPlace+1] == 'x'
    or cpuMatrix[numberPlace][letterPlace+2] == 'x'):
        print("cpu placed WRONG")

        letterPlace= random.randint(letterLeftBorder,letterRightBorder-2)
        numberPlace = random.randint(numberUpBorder,numberDownBorder)
        print("cpu placed in "+ str(chr(letterPlace+64)) + ", " + str(numberPlace))

    cpuMatrix[numberPlace][letterPlace] = 'x'
    cpuMatrix[numberPlace][letterPlace+1] = 'x'
    cpuMatrix[numberPlace][letterPlace+2] = 'x'

print("\n")
print("-- User Matrix --")
for s in userMatrix:
    print(*s)

print("\n")
print("-- Cpu Matrix (VISIBILE ONLY IN DEBUG) --")
for s in cpuMatrix:
    print(*s)
#3-BLOCK SHIP PLACEMENT###

userPlaying = True;
turn = 0
#GAME LOOP
while(gamestate != 0):

    turn= turn + 1
    print("\n- - - -TURN "+str(turn)+" - - - -\n")

    if(userPlaying):#USER'S TURN
        print("\nChoose your target..\n")
        w = dict[input("Enter letter: ")]
        h = int(input("Enter number: "))
        while(w > letterRightBorder or w < letterLeftBorder or
        h > numberDownBorder or h < numberUpBorder):
                print("\n-- You can't hit out of border. Choose your target --\n")
                w = dict[input("Enter letter: ")]
                h = int(input("Enter number: "))

        if(cpuMatrix[h][w]=='x'):
            print("\nship hit!")
            userHitMatrix[h][w] = 'x'
            cpuDamagedMatrix[h][w] = 'x'

            if(cpuDamagedMatrix == cpuMatrix):
                gamestate = 0
                print("\nYou win!")
            else:
                print("\n-- Your HitMatrix --")
                for s in userHitMatrix:
                    print(*s)
        else:
            print("\nnothing...")
            userHitMatrix[h][w] = '1'
            print("\n-- Your HitMatrix --")
            for s in userHitMatrix:
                print(*s)
            userPlaying = False

    else:#CPU'S TURN
        print("\nCPU playing..\n")
        w= random.randint(letterLeftBorder,letterRightBorder)
        h = random.randint(numberUpBorder,numberDownBorder)
        while(cpuHitMatrix[h][w] == 'x' or
        cpuHitMatrix[h][w] == '1'):
            w= random.randint(letterLeftBorder,letterRightBorder)
            h = random. randint(numberUpBorder,numberDownBorder)

        if(userMatrix[h][w]=='x'):
            print("\nCPU hit your ship!")
            cpuHitMatrix[h][w] = 'x'
            userDamagedMatrix[h][w] = 'x'

            if(userDamagedMatrix == userMatrix):
                gamestate = 0
                print("\nCPU win!")
                print("\n-- CPU HitMatrix --")
                for s in cpuHitMatrix:
                    print(*s)
        else:
            print("\ncpu Missed...")
            cpuHitMatrix[h][w] = '1'
            print("\n-- CPU HitMatrix --")
            for s in cpuHitMatrix:
                print(*s)
            userPlaying = True


    #RENDER