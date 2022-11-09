import random
randomNumber = random.randint(1,100)
win = False
while (not win):
    guess = input("Guess a number between 1-100: ")
    diff = abs(int(guess) - randomNumber)
    if(diff == 0):
        print("You guessed the right number!")
        win = True
    else:
        print("You were " + str(diff) + " off")
8