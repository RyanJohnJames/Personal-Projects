import random

userwin = 0
computerwin = 0

options = ["rock", "paper", "scissors"]


while True:
    
    print("You won " + str(userwin) + " times and the computer won " + str(computerwin) + " times.")
    userinput = input("Type Rock/Paper/Scissors or type Esc to quit. : ").lower()
    if userinput == "esc":
        break #Player leaves the game and code ends.
    
    #checks if the player did input anything other than rock paper scissor, if yes, go back to asking them.    
    elif userinput not in options: 
        continue

    random_number = random.randint(0, 2)
    # Rock: 0 Paper: 1 Scissors: 2
    computerpick = options[random_number]

    print("Computer picked ", computerpick + ".")

#checking win conditions, I know this can be easier but Im not that good.
    if userinput == "rock" and computerpick == "scissors":
        print("You win!")
        userwin += 1
        continue
    elif userinput == "paper" and computerpick == "rock":
        print("You win!")
        userwin += 1
        continue
    elif userinput == "scissors" and computerpick == "paper":
        print("You win!")
        userwin += 1
        continue
    else:
        print("You lost!")
        computerwin += 1

print("Thanks for playing! Goodbye!")
    
