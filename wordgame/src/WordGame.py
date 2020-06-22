# Load Libraies
import pandas as pd
import making_word_data as game_func

# A Guess the word game using for loops and if/else statments

# Setup Game
needs_setup = input("Do you need to setup the game? (Y/N)")

if needs_setup == "Y":
    game_func.game_setup()

run_game = input("Do you want to play? ")

if run_game == "Y":
    game_data = pd.read_csv("GameFile.csv")
    # number_rounds = int(input("How mnay times to do you want to play? "))
    score = 0

    for rounds in range(len(game_data)):
        # the_word = input("What word are you think about? " ) #"frogs"
        # hint = input("What is your hint? ")
        guess_is_right = False
        guessed_word = ""
        # number_of_guess = int(input("How many tries? ")) #3
        
        # Learning Input
        # user_value = input("Say something: ") 
        # print(user_value)
        print("Hint:", game_data.Hint[rounds])

        for guess in range(game_data.Lives[rounds]):
            
            guessed_word = input("Guess the word am thinking about: ")

            if guessed_word == game_data.Word[rounds]:
                print("You have guessed correclty")
                score = score + 1
                break
            else:
                print("That guess was incorrect")
        
        if rounds == (len(game_data) - 1):
            print("Your Score is : ",score, "You Played ",len(game_data))
        else:
            print("=================")
            print("=== Next Game ===")




