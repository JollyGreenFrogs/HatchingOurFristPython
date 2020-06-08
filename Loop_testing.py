# Some Looping examples, and how to use them.

got_it_right = False

guess_word = "Hello"

for number in range(3):
    # Everything in the indent will be in the loop
    # Print out the number
    user_word = input("Guess the word:")
    if guess_word == user_word:
        got_it_right = True

print("You go the word",got_it_right)





