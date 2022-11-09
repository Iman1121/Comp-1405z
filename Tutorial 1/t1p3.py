import random
randomNumber = random.randint(1,100)
guess = input("Guess a number between 1-100: ")
diff = abs(int(guess) - randomNumber)
if(guess == randomNumber):
    print("You guessed the right number!")
else:
    print("You were " + str(diff) + " off")
    