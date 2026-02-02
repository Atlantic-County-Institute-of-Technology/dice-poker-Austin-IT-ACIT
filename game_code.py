from die import Dice
from display import face_icons
import os
import inquirer3
import time

rolled = 0
attempts = 3 - rolled

dices_final = [0, 0, 0, 0, 0]
dice = Dice()
GAME = True
outer_roll = 0

def prompt_list_message(in_message, in_choices):
    # prompt question from input
    question = [
        inquirer3.List(
            "choice",
            message=in_message,
            choices=in_choices,
        ),
    ]
    # parse and return the response
    answer = inquirer3.prompt(question)
    # clears the terminal on both windows and linux
    os.system('cls' if os.name == 'nt' else 'clear')
    return answer["choice"]

# function to change the list "keeped" when wanted
def change_keeped():
    global number, dices_final
    if dice.keep[number] == dices_final[number]:
        dice.keep[number] = 0
    else:
        dice.keep[number] = dices_final[number]
    
# the start of the MAIN python code
def Main():
    print("""
                     .=-.-.    _,.----.         ,----.              _ __        _,.---._      ,--.-.,-.        ,----.               
      _,..---._     /==/_ /  .' .' -   \     ,-.--` , \          .-`.' ,`.    ,-.' , -  `.   /==/- |\  \    ,-.--` , \   .-.,.---.  
    /==/,   -  \   |==|, |  /==/  ,  ,-'    |==|-  _.-`         /==/, -   \  /==/_,  ,  - \  |==|_ `/_ /   |==|-  _.-`  /==/  `   \ 
    |==|   _   _\  |==|  |  |==|-   |  .    |==|   `.-.        |==| _ .=. | |==|   .=.     | |==| ,   /    |==|   `.-. |==|-, .=., |
    |==|  .=.   |  |==|- |  |==|_   `-' \  /==/_ ,    /        |==| , '=',| |==|_ : ;=:  - | |==|-  .|    /==/_ ,    / |==|   '='  /
    |==|,|   | -|  |==| ,|  |==|   _  , |  |==|    .-'         |==|-  '..'  |==| , '='     | |==| _ , \   |==|    .-'  |==|- ,   .' 
    |==|  '='   /  |==|- |  \==\.       /  |==|_  ,`-._        |==|,  |      \==\ -    ,_ /  /==/  '\  |  |==|_  ,`-._ |==|_  . ,'. 
    |==|-,   _`/   /==/. /   `-.`.___.-'   /==/ ,     /        /==/ - |       '.='. -   .'   \==\ /\=\.'  /==/ ,     / /==/  /\ ,  )
    `-.`.____.'    `--`-`                  `--`-----``         `--`---'         `--`--''      `--`        `--`-----``  `--`-`--`--' 
        
        
        """)

    #all needed globals
    global number, rolled, attempts, dices_final
    
    # sets the dices_final to nothing
    dices_final = [0, 0, 0, 0, 0]

    # rolls dice and sets them into dices_final
    for i in range(len(dices_final)):
        dices_final[i] = dice.dice[i].roll()

    # ask the question if wanted to play
    response = prompt_list_message("Please choose an option :", ["Play Game", "Exit"])
    match response:

        # starts the code to play the game
        case "Play Game":
            play_game()
              
        # exits the code and does nothing else
        case "Exit":
            exit()

# the code to play the game
def play_game():

    # all global objects needed
    global number, rolled, attempts, outer_roll, dices_final, GAME

    # # sets the game to true to start the game
    # GAME = True

    # set the "winning" list to nothing
    winning = [0, 0, 0, 0, 0, 0]
    
    # adds a number due to the game rolling the dice already
    rolled += 1

    # when ever the "GAME" is active it will run this code as long as it is
    while GAME:
        global dices_final

        # changes the amount of attempts you have from each roll
        attempts = 3 - rolled

        # when rolled is less then or equal to 3 (max amount of rolls) it will run this code
        while rolled < 3: 

            # shows the amount of times rolled and how many attempts are left.
            print(f" [!] Times rolled: {rolled} || Attempts: {attempts} [!]")
            print(f"Keeped dice: {dice.keep}")
           
            # print the faces of the dice
            print(  f"[-] Dice #1: {dices_final[0]} [-]\n"
                f" {face_icons[dices_final[0]-1]}\n"

                f"[-] Dice #2: {dices_final[1]} [-]\n"
                f" {face_icons[dices_final[1]-1]}\n"

                f"[-] Dice #3: {dices_final[2]} [-]\n"
                f" {face_icons[dices_final[2]-1]}\n"

                f"[-] Dice #4: {dices_final[3]} [-]\n"
                f" {face_icons[dices_final[3]-1]}\n"

                f"[-] Dice #5: {dices_final[4]} [-]\n"
                        f" {face_icons[dices_final[4]-1]}\n")
                    
            # gives options to keep diffrent dice and to roll the dice.
            response = prompt_list_message("Please choose an option :", [ "[-] ROLL", "[-] DONE", "[-] Keep Dice #1", "[-] Keep Dice #2", "[-] Keep Dice #3", "[-] Keep Dice #4", "[-] Keep Dice #5"])
            match response:

                case "[-] Keep Dice #1":
                    number = 0
                    change_keeped()

                case "[-] Keep Dice #2":
                    number = 1
                    change_keeped()

                case "[-] Keep Dice #3":
                    number = 2
                    change_keeped()

                case "[-] Keep Dice #4":
                    number = 3
                    change_keeped()
                case "[-] Keep Dice #5":
                    number = 4
                    change_keeped()

                case "[-] ROLL":

                    rolled += 1
                    attempts = 3 - rolled
                    outer_roll = 0

                    # while outer_roll is less then or equal to 5 it will run (each time it rolls it is "animated" for when it is rolled)
                    while outer_roll <= 5:

                        # goes through each dice and if the number in dice.dice is equal to index the in dices_final it will roll that dice
                        for i in range(len(dice.keep)):

                            if dice.keep[i] == 0:
                                dices_final[i] = dice.dice[i].roll()

                        # print the dices faces
                        print(  f"[-] Dice #1: {dices_final[0]} [-]\n"
                        f" {face_icons[dices_final[0]-1]}\n"

                        f"[-] Dice #2: {dices_final[1]} [-]\n"
                        f" {face_icons[dices_final[1]-1]}\n"

                        f"[-] Dice #3: {dices_final[2]} [-]\n"
                        f" {face_icons[dices_final[2]-1]}\n"

                        f"[-] Dice #4: {dices_final[3]} [-]\n"
                        f" {face_icons[dices_final[3]-1]}\n"

                        f"[-] Dice #5: {dices_final[4]} [-]\n"
                        f" {face_icons[dices_final[4]-1]}\n")


                        outer_roll += 1
                        time.sleep(0.35)
                        os.system('cls' if os.name == 'nt' else 'clear')


                    # if rolled is equal to 3 it will stop the game from running
                    if rolled == 3:
                        GAME = False

                # of DONE is selected then it will equal rolled to 3 and make GAME false
                case "[-] DONE":
                    rolled = 3
                    GAME = False

        if rolled == 3:
                    # changes the winning statment to nothing 
                    winning = [0, 0, 0, 0, 0, 0]

                    # sets the list "winning" to diffrent numbers from the faces of the dice
                    for i in range(len(dices_final)):
                        if dices_final[i] == 1:
                            winning[0] += 1
                        if dices_final[i] == 2:
                            winning[1] += 1
                        if dices_final[i] == 3:
                            winning[2] += 1
                        if dices_final[i] == 4:
                            winning[3] += 1
                        if dices_final[i] == 5:
                            winning[4] += 1
                        if dices_final[i] == 6:
                            winning[5] += 1

                    # if you have 5 dice with the same face
                    if 5 in winning:
                        winning_quote = "You have a Five of a kind"

                    # if you have 4 dice with the same face
                    elif 4 in winning:
                        winning_quote = "You have a Four of a kind"

                    # if you have 3 dice with the same face and 2 dice of the same fice
                    elif 3 in winning and 2 in winning:
                        winning_quote = "You have a Full House"

                    # if you have 5 dice counting from lowest to highest without a skip
                    elif winning.count(1) == 5 and winning.count(0) == 1:
                        winning_quote = "You have a Straight"

                    # if you have 3 dice with the same face
                    elif 3 in winning:
                        winning_quote = "You have a Three of a kind"

                    # if you have 2 dice with the same face with another set of dice with the same face
                    elif winning.count(2) == 2:
                        winning_quote = "You have a Two pairs"

                    # if you have 2 dice with the same face
                    elif 2 in winning:
                        winning_quote = "You have a Two of a kind"

                    # if you have gotten non avalible winning option
                    else:
                        winning_quote = "You have lost... some how"


                    # print the faces of the die and the number of the die
                    print(f"[-] Dice #1: {dices_final[0]} [-]\n"
                    f" {face_icons[dices_final[0]-1]}\n"

                    f"[-] Dice #1: {dices_final[1]} [-]\n"
                    f" {face_icons[dices_final[1]-1]}\n"

                    f"[-] Dice #1: {dices_final[2]} [-]\n"
                    f" {face_icons[dices_final[2]-1]}\n"

                    f"[-] Dice #1: {dices_final[3]} [-]\n"
                    f" {face_icons[dices_final[3]-1]}\n"

                    f"[-] Dice #1: {dices_final[4]} [-]\n"
                    f" {face_icons[dices_final[4]-1]}\n")

                    #shows the words "GAME OVER"
                    print("GAME OVER")

                    # shows what way you have won or lost.
                    print(winning_quote)

                    # makes the options to play the code again (restarts the code) or quit (ends the code)
                    response = prompt_list_message("Please choose an option :", ["[-] Play Again", "[-] Exit"])
                    match response:

                        case "[-] Play Again":

                            rolled = 0
                            
                            # changes the keeped dice to equal nothing
                            for i in range(len(dice.keep)):
                                dice.keep[i] = 0
                            # rerolls all the dice before the game is being played
                            for i in range(dice.max_dice):
                                dices = dice.dice[i].roll()
                                dices_final[i] = dices

                            #sets the GAME to true
                            GAME = True
                                
                            # activates the game again to play the game once again.
                            play_game()

                        # exits the code and ends the script
                        case "[-] Exit":

                            exit()


if __name__ == '__main__':
    Main()