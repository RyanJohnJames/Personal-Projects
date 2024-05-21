#credit = 100
#random.int 0 - 36
#to check if odd or even num % 2 == 0
#1. bet money
#2. guess if odd or even
#3. roll d36
#4. check if odd or even
#5. see if the person guess correct, if yes give money, if no take money
#6. repeat until man becomes broke or 0 dollars
import random
credit = 100
while credit > 0:
    number = random.randint(0, 36)
    #print(number)
    try:
        bettingmoney = int(input("How much money would you like to bet? You have " + str(credit) + ": "))
        if credit - bettingmoney < 0:
            
            print("Your input is incorrect! Please try again")
        else:
            guessingnum = input("Is the number gonna be odd or even?: ")
            if guessingnum.upper() == "ODD" or guessingnum.upper() == "EVEN":   
                if number % 2 == 0:
                    a = "even"
                else:
                    a = "odd"
                if a.upper() == guessingnum.upper():
                    print("You are correct!")
                    credit = credit + bettingmoney
                else:
                    print("You are wrong!")
                    credit = credit - bettingmoney
            else:
                print("Unknown value, please try again.")
    except:
        print("Please input a vaild value.")

    
