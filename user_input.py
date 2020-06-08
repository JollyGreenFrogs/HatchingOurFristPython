# script to get user imput and print it back out to the console 
def userinput():
    #getting user imput
    hello = input("Give me a message:")
    world = input("Give me another message:")
    #print user imput
    print(hello)
    print(world)
    print (type(hello))
    print(hello,world)

    # print (type(hello))
# DocString
print("1st Time I called Function")
userinput()


print("2nd Time I Called the function")
userinput()