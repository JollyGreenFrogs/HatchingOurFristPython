# This is the Game data object
import pandas as pd

class game_data:
    """
        Games data class. 
    """
    def __init__(self, number_round=0):
        """
        Initialize all the variable I need
        """

        self.word_list = []
        self.game_number_list = []
        self.hint_list = []
        self.number_tries = []
        self.number_rounds=number_round
    
    def game_setup(self):
       """
       Function will put together all the lists into a data frame
       """ 

       df = pd.DataFrame( {
            "GameNumber":self.game_number_list,
            "Word":self.word_list,
            "Hint":self.hint_list,
            "Lives":self.number_tries
        })
       df.to_csv("data\GameFile.csv")
    
    def added_word_list(self,new_word):
        """
        Added the next word
        """
        self.word_list.append(new_word)
    
    def added_game_number(self,game_number):
        """
        Added the next word
        """
        self.game_number_list.append(game_number)
    
    def added_hint_list(self,new_hint):
        """
        Added the next word
        """
        self.hint_list.append(new_hint)
    
    def added_number_of_tries(self,tries):
        """
        Added the next word
        """
        self.number_tries.append(tries)