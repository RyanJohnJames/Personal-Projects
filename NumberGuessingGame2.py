import random


topofrange = input("Type a number: ")

if topofrange.isdigit():
    topofrange = int(topofrange)

    if topofrange <= 0:
        print("Please type a number larger then 0.")
        quit()
else:
    print("Please type a number larger then 0.")
    quit()
    

randnum = random.randrange(0, topofrange)

while True:
    userguess = input("Make a guess: ")
    if userguess.isdigit():
        userguess = int(userguess)
    else:
        print("Please type a number next time!")
        continue

    if userguess == randnum:
        print("You got it! YAY!")
        break
    else:
        print("Too bad! You got it wrong!")
    
