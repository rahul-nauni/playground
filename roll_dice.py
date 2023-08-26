import random
guess = ""
roll = True
while True:
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    score = dice1 + dice2
    guess = input("What is the total (2-12)? ")
    if guess == str(score):
        print("You got it!")
        break 
    else:
        print("Nope! It was " + str(score))
        #roll = input("Roll again? (y/n) ") == "y"