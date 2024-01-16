# this is project 3 
# tic tac toe game 
def sum(a,b,c):
    return a + b + c
def printBoard(xstate , zstate): 
    zero = 'x' if xstate[0] else ('o' if zstate[0]else 0)
    one = 'x' if xstate[1] else ('o' if zstate[1]else 1)
    two = 'x' if xstate[2] else ('o' if zstate[2]else 2)
    three = 'x' if xstate[3] else ('o' if zstate[3]else 3)
    four = 'x' if xstate[4] else ('o' if zstate[4]else 4)
    five = 'x' if xstate[5] else ('o' if zstate[5]else 5)
    six = 'x' if xstate[6] else ('o' if zstate[6]else 6)
    seven = 'x' if xstate[7] else ('o' if zstate[7]else 7)
    eight = 'x' if xstate[8] else ('o' if zstate[8]else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")



if __name__ == "__main__":   #with this code we can ensure that when our code is importing only main functions of it are inmporting code is not running
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 #1 for x and 0 for o
    print("welcome to tic tac toe")
    while(True):
        printBoard(xstate , zstate)
        if (turn == 1):
            print ("x's chance ")
            value = int(input("please enter a number : "))
            xstate[value] = 1
    
        else:
            print ("o's chance")
            value = int(input("please enter a value : "))
            zstate[value] = 1

        turn = 1 - turn
