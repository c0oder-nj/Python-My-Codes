import random
randnumber = random.randint(1,100)

userGuess = None
guessesNumber = 0
while(userGuess != randnumber):
    guessesNumber   = guessesNumber + 1
    userGuess = int(input("Enter your Guess user: "))
    if(userGuess == randnumber):
        print("You guess it correct")
    else:
        if(userGuess>randnumber):
            print("Please choose Smaller Number User ")
        else:
            print("Please choose Greater Number User")
    
print(f"You took {guessesNumber} number of guesses to find out answer..." )

# print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guessesNumber<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guessesNumber))

