#Lauren Bowman
#Lab 7
#Extra Credit

NUMBER = 3
 

keepguessing = True

while keepguessing:

    guess = int(input("Hello! Guess a number between 1-10: "))
    
    if guess == NUMBER:
        print ("Yay! You guessed correctly!")
        keepguessing = False

    elif guess - NUMBER <= 2 and guess - NUMBER >= -2:
        print("Oh no! Try again: ")

    elif guess > NUMBER:
        print ("Oh no- you lost! I'm sorry your guess was higher than my number which is", NUMBER)
        keepguessing = False
    else:
        print ("I'm sorry, looks like you lost.Your guess was lower than my number which is", NUMBER)
        keepguessing = False

