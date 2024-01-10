import random
randnumber = random.randint(1,100)
userguess = None
guesses = 0
while (userguess != randnumber):
    userguess = int(input("enter your guess: "))
    guesses += 1
if (userguess==randnumber):
    print ("you guessed it right! ")
else:
    if (userguess>randnumber):
        ("you guessed it wrong! enter a smaller number")
    else:
        print ("you guessed it wrong! enter a larger number")
    
print (f"you guessed the number in {guesses} guesses")
with open ("highscore.txt","r") as  f:
    hiscore = int (f.read())

if (guesses<hiscore):
    print ("you have just broken the high score!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))