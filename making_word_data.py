# Libary Imports
import pandas as pd

def game_setup():
    # Setting up our game. 
    word_list = []
    game_number_list = []
    hint_list = []
    number_trys = []

    number_rounds = int(input("How mnay times to do you want to play? "))

    for rounds in range(number_rounds):

        word_list.append(input("Whats the word? ")) # Adding word to word_list
        game_number_list.append(rounds) # Adding to the game number list
        hint_list.append(input("Whats the hint? ")) # Adding to the hint list
        number_trys.append(int(input("How many tries? "))) # Adding to the number of tries


    df = pd.DataFrame( {
        "GameNumber":game_number_list,
        "Word":word_list,
        "Hint":hint_list,
        "Lives":number_trys
    })

    df.to_csv("GameFile.csv")
