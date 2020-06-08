# A Guess the word game using for loops and if/else statments

# Setup Variables
number_rounds = int(input("How mnay times to do you want to play? "))
score = 0
for rounds in range(number_rounds):
    the_word = input("What word are you think about? " ) #"frogs"
    hint = input("What is your hint? ")
    guess_is_right = False
    guessed_word = ""
    number_of_guess = int(input("How many tries? ")) #3
    
    # Learning Input
    # user_value = input("Say something: ") 
    # print(user_value)
    print("Hint:", hint)

    for guess in range(number_of_guess):
        
        guessed_word = input("Guess the word am thinking about: ")

        if guessed_word == the_word:
            print("You have guessed correclty")
            score = score + 1
            break
        else:
            print("That guess was incorrect")
    
    if rounds == (number_rounds - 1):
        print("Your Score is : ",score, "You Played ",number_rounds)
    else:
        print("=================")
        print("=== Next Game ===")

