print("Welcome to Rock_Paper_Scissors world\n\n")

import random

a = int(input('Your turn : Select "[1]_for_Rock", "[2]_for_paper", "[3]_for_scissors"  '))

b = random.randint(1, 3)


####################################################

if a == 1:
    print("You choose - Rock")
elif a == 2:
    print("You choose - Paper")
else:
    print("You choose - Scissors")


#####################################################

if b == 1:
    print("Computer choose - Rock")
elif b == 2:
    print("Computer choose - Paper")
else:
    print("Computer choose - Scissors")




#####################################################

if b == 1:
    if a == 2:
        print("You win")
    elif a == 3:
        print("You loose")
    else:
        print("It's a Draw")

if b == 2:
    if a == 1:
        print("You Loose")
    elif a == 3:
        print("You win")
    else:
        print("It's a Draw")

if b == 3:
    if a == 2:
        print("You loose")
    elif a == 3:
        print("It's a Draw")
    else:
        print("You win")


print("Thank You!")
