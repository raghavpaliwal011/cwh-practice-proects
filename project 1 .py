import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("comp turn : snake(s) water(w) gun(g)?")
randno=random.randint(1,3)
print(randno)
if randno==1:
    comp='s'

elif randno==2:
    comp='w'

elif randno==3:
    comp='g'

a=("your turn: snake(1) water(w) gun(g)?")
gamewin (comp, a)
if a == None:
    print("the game is a tie")

elif a:
    print("you win")

else:
    print("you lose")

   