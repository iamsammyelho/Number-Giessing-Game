import random
import time


# Displays game instruction
def display_info():
    display = """WELCOME TO THE \"GUESS NUMBER GAME\"
            HOW IT WORKS:
                      I WILL GENERATE A RANDOM NUMBER BETWEEN 1-10
                      YOU HAVE FIVE TRIES TO GUESS IT CORRECTLY
                      
                      LET THE GAME BEGIN>>>>"""
    # printing out the display text word by word
    for read in display:
        print(read, end="", flush=True)
        time.sleep(0.1)
    print("\n\n................")
    time.sleep(3)

# Generating a random number 1 - 10
def gnrt_num():
    number = random.randint(1, 10)
    return number


# Printing an error message
def error_msg(value):
    if value == "int":
        print("\nERROR INPUT!!\nYou can only enter digits for this input")
    elif value == "str":
        print("\nERROR INPUT!!\nYou can only enter \"Y\" or \"N\" for this input")


# Getting the player's input and handling the game's conditions
def player():
    tries = 1
    correct = gnrt_num()
    print("\n\n I have chosen a random number")
    print("Try your best to guess it")
    while True:
        try:
            guess = int(input("\nTake a guess: "))
            if guess == correct:
                print("\nNicely done !")
                print(f"The correct number was {correct} and you guessed it correctly\nin {tries} tries")
                break
            elif guess > correct:
                print("\nNope !\nTry a lower guess.")
                if tries == 4:
                    print("\nNope !\nYou have one last try left.")
                    tries += 1
                    continue
                elif tries == 6:
                    print("\nSorry !\nYou have run out of tries.")
                    break
                tries += 1
                continue
            elif guess < correct:
                print("\nNope !\nTry a higher guess.")
                if tries == 4:
                    print("\nNope !\nYou have one last try left.")
                    tries += 1
                    continue
                elif tries == 5:
                    print("\nSorry !\nYou have run out of tries.")
                    break
                tries += 1
                continue
            else:
                print("\nSomething went wrong !")
                break
        except ValueError:
            error_msg("int")
            continue


# Putting them together
def main():
    display_info()
    player()
    while True:
        try:
            choice = str(input("\n\nWould you like to play again ?"))
            if choice.lower() == "y":
                player()
                continue
            elif choice.lower() == "n":
                print("\nWe had a funtime\nI do hope you come back again ")
                break
            elif choice.lower() not in ("y", "n"):
                error_msg("str")
                continue
            else:
                print("\nSomething went wrong !")
                break
        except ValueError:
            error_msg("str")
            continue


# Starting the program
main()
