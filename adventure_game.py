import time
import random

# Function to decrease the number of "time.sleep" in the code
def print_pause(message):
    print(message)
    time.sleep(1)

# Function to allow the player to play again at the end or end the game
def game_over():
    while True:
        replay = input("Do you want to play again? (y/n): ")
        if replay == "y":
            global score
            score = 0
            play_game()
            return False
        elif replay == "n":
            print_pause("Thanks for playing! Hope you enjoyed.")
            return False
        else:
            print_pause("Invalid input, please enter 'y' or 'n'.")

# 3 Functions to check if the player wins or not
def check_win():
    if score >= 100:
        print_pause("Congrats, You have maxed the score!")
        print_pause("You have finished the game!!")
        game_over()
        return True
    return False
# Function to check if he lost or not
def check_lose():
    if score <= -50:
        print_pause("Your score has dropped to -50 or less.")
        print_pause("You have lost the game.")
        game_over()
        return True
    return False
# Function to let him continue if he has the normal score
def continue_game():
    if score > -50 and score < 100:
        print_pause("You are going to start the next round")
        print_pause("Your goal is to reach 100 points")
        print_pause(f"Good luck you have {score} points")
        play_game()
    return False

# Function to explain to the player what is happening and tell him choices
def house():
    global has_sword, score
    print_pause("You have chosen to enter the big house.")
    print_pause("You knock on the door... no one answers.")
    print_pause("You find the door unlocked already.")
    print_pause("You enter the house and find a witch.")
    print_pause("The witch is doing some magic in the corridor.")
    print_pause("Enter 1 to attack the witch with your sword.")
    print_pause("Enter 2 to run away back to where you came from.")
    while True:
        house_choice = input("Please choose 1 or 2: ")

        if house_choice == "1":
            print_pause("You decided to attack the witch.")
            print_pause("She started doing some spells.")
            if has_sword:
                score += 50
                print_pause("The witch is defeated by your magical sword!")
                print_pause("You have gained 50 points")
                print(f"Your score: {score}")
                if check_win():
                    return True
                else:
                    continue_game()
                    return True
            else:
                score -= 20
                print_pause("The witch seems not damaged by the sword.")
                print_pause("She uses her magical staff.")
                print_pause("The witch has defeated you.")
                print_pause("You have lost 20 points.")
                print(f"Your score: {score}")
                if check_lose() or check_win():
                    return True
                else:
                    continue_game()
                    return True
        elif house_choice == "2":
            outcome = random.choice(["survive", "die"])
            if outcome == "survive":
                score += 20
                print_pause("You hardly escaped and ran away to the forest.")
                print_pause("You stood for a bit and took a breath.")
                print_pause("Enter 1 to go back to the house")
                print_pause("Enter 2 to go to the underground cave")
                print_pause("You have gained 20 points.")
                print(f"Your score: {score}")
                return True
            else:
                score -= 20
                print_pause("As you run away, the witch casts a spell.")
                print_pause("You have been hurt.")
                print_pause("The witch has defeated you.")
                print_pause("You lost 20 points.")
                print(f"Your score: {score}")
                if check_lose() or check_win():
                    return True
                else:
                    continue_game()
                    return True
        else:
            print("Invalid input, please choose 1 or 2 to continue.")

# Func for the 2nd time the player comes from the cave & asks him where to go
def forest_2():
    global has_sword, score
    print_pause("Enter 1 to enter the big house.")
    print_pause("Enter 2 to enter the underground cave.")
    while True:
        forest2_choice = input("Please choose 1 or 2: ")
        if forest2_choice == "1":
            house_result = house()
            if not house_result:
                return False
        elif forest2_choice == "2":
            if has_sword:
                print_pause("You went there already & got the magical sword.")
            else:
                cave_result = cave()
                if not cave_result:
                    return False
        else:
            print("Invalid input, please choose 1 or 2 to continue.")

# Function to explain to the player what is happening
def cave():
    global has_sword, score
    print_pause("You have chosen to enter the underground cave.")
    print_pause("You enter the cave and find a magical sword.")
    print_pause("Enter 1 to pick it up and return to the forest.")
    print_pause("Enter 2 to return to the forest and ignore it.")
    while True:
        cave_choice = input("Please choose 1 or 2: ")
        if cave_choice == "1":
            has_sword = True
            score += 30
            print_pause("You picked up the magical sword.")
            print_pause("You feel more overpowered than ever!")
            print_pause("You have gained 30 points")
            print(f"Your score is: {score}")
            return forest_2()
        elif cave_choice == "2":
            print_pause("You decided to ignore the magical sword")
            print_pause("You have returned to the forest.")
            return forest_2()
        else:
            print("Invalid input, please choose 1 or 2 to continue.")

# Function to start the game
def play_game():
    global has_sword, score
    has_sword = False
    print_pause("You find yourself standing in a magical forest.")
    print_pause("Rumors say that there is a magical sword roaming here.")
    print_pause("They say it has very powerful strength.")
    print_pause("On your left, you find a big house.")
    print_pause("You hear a laughing from it.")
    print_pause("On your right, you find an underground cave.")
    print_pause("You see a glimpse of light.")
    print_pause("Enter 1 to enter the big house.")
    print_pause("Enter 2 to enter the underground cave.")
    while True:
        choice = input("Please choose 1 or 2: ")
        if choice == "1":
            house_result = house()
            if not house_result:
                return
            break
        elif choice == "2":
            cave_result = cave()
            if not cave_result:
                return
            break
        else:
            print("Invalid input, please choose 1 or 2 to continue.")
score = 0
play_game()