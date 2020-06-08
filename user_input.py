# Script to get user input and print it back out to the console
def userinput():
    # Getting user input
    hello = input("Give me a message: ")
    world = input("Give me another message:")
    # Print out user input
    print(hello)
    print(world)

    print(hello,world)

    # print(type(hello))

# DocString
print("1st Time I called function")
userinput()

print("2nd Time I called the function")
userinput()
