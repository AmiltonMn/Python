from random import randint
continuar = 1
jogadas = {1:"ROCK", 2:"PAPER", 3:"SCISSORS"}
x = 0

def RPS():
    draws = 0
    wins = 0
    loses = 0
    winstreak = 0
    while continuar !=0:  
        print("|-=---=---=---=---=---=---=---=-\n")
        print("|-=    ROCK PAPER SCISSORS    =-\n")
        print("|-=---=---=---=---=---=---=---=-\n")
        print("You will play against the computer!\n")
        print(f"DRAWS: {draws}. WINS {wins}. LOSES {loses}\n")
            print(f"WINSTREAK: {winstreak}")
        x = 0
        while x <= 0 or x > 3:
            computerPlay = randint(1, 3)
            try:
                print("Press 1 for ROCK\nPress 2 for PAPER\nPress 3 for Scissors\nPress 0 to leave")
                x = int(input("Choose your play!\n"))
                print(f"{jogadas[x]}")
                if x <= 0 or x > 3:
                    raise ValueError
                else:
                    if computerPlay == x:
                        print("Draw!\n")
                        draws += 1
                        winstreak  = 0
                        break
                    if x - 1 == computerPlay:
                        print("You win!\n")
                        wins += 1
                        winstreak += 1
                        break
                    if x + 1 == computerPlay:
                        print("You lose!\n")
                        loses += 1
                        winstreak = 0
                        break
                    if x == 3 and computerPlay == 1:
                        print("You lose!\n")
                        loses += 1
                        winstreak = 0
                        break
                    if x == 1 and computerPlay == 3:
                        print("You win!\n")
                        wins += 1
                        winstreak += 1
                        break
            except ValueError:
                print("Please choose a number between 1 and 3!\n")
                print("Press 1 for ROCK\nPress 2 for PAPER\nPress 3 for Scissors\n")
                x = int(input("Choose your play! "))
            except x = 0:
                continuar = 0
                break
        
