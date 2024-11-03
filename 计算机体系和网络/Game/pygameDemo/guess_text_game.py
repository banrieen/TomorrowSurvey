from random import randint
import re

def option():
    option = str(input("Continue to guess Yes or No ? "))
    if re.match(option, "Yes|yes"):
        return True
    else:
        return False

def guess_game():
    x = randint(1,100)
    guess = -1
    print("Guess the number below 1 ~ 100 : ")
    while guess != x and option():
        guess = int(input("Guess:　"))
        if guess != x:
            print("Wrong guess number !")
        else:
            print("Guessed correctly")


guess_game()
if __name__ == "__mian__":
    guess_game()