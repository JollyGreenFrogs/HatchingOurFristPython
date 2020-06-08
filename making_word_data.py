import pandas as pd 

def game_setup():
    word_list = []
    game_number_list = []
    hint_list = []
    number_trys = []

    number_rounds = int(input("how many times do you want to play"))

    for rounds in range(number_rounds):
        word_list.append(input("whats the word?"))
        game_number_list.append(rounds)
        hint_list.append(input("whats the hint?"))
        number_trys.append(int(input("how many tries?")))
    
    df = pd.DataFrame( {
        "gamenumber":game_number_list,
        "word":word_list,
        "hint":hint_list,
        "lives":number_trys
    })


    df.to_csv("gamefile.csv")