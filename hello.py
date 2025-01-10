import random
keepGoing = True
play = input("Would you like to play a game? (Y/N): ")
play = play.lower()
if play[0]=="y":
    bal = 100
    print("You are playing roulette, your starting balance is 100. Enter q or quit for the color when you are done")
    while keepGoing:
        print(f"your balance: {bal}")
        bet = input("How much would you like to bet?: ")
        if bet.isdigit():
            bet = int(bet)
            color = input("Choose red, black, or green: ")
            color = color.lower()
            wheelResult = random.randint(1,38)
            if bet<=bal:
                if wheelResult<19:
                    if color[0]=="r":
                        print("It landed on red, you win!")
                        bal += bet
                    else:
                        print("It landed on red, you lost")
                        bal -= bet
                if wheelResult>18:
                    if wheelResult<37:
                        if color[0]=="b":
                            print("It landed on black, you win!")
                            bal += bet
                        else:
                            print("It landed on black, you lose")
                            bal -= bet
                    else:
                        if color[0]=="g":
                            print("It landed on green, you win!")
                            bal += 17*bet
                        else:
                            print("It landed on green, you lose")
                            bal -= bet
                if color[0]=="q":
                    keepGoing = False
                if bal==0:
                    tryAgain = input("You ran out of money. Do you want to try again? Y/N: ").lower()
                    if tryAgain[0] == "y":
                        bal = 100
                    else:
                        keepGoing = False

            else:
                print("Your bet exceeded your balance")
        else:
            print("Your bet should be an integer")
