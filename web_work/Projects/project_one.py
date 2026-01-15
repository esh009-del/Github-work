#hello world
print("Hello User")
print("You will be set a secret number that is not shown to you ")
print("You will have to guess the number ")

import random 
random_integer=random.randint(1, 10)
chances= 3

for i in range(chances):
    user_input=int(input("what number do you guess"))
    if random_integer > user_input:
        print("too big ")
        chances=chances-1
        print(chances ,"chances left")
    elif random_integer < user_input:
        print("Too small")
        chances=chances -1 
        print(chances ,"chances left")
    elif random_integer == user_input:
        print("Correct")
        print("you have " , chances ,  "chances left")
    
    elif chances == 0:
        print("You lost with", chances , "chances left")
    
    else:
        print("Invalid input")

    
print("Thanks for playing ")
print("shush")
    