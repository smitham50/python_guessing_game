import random

random_num = random.randint(1,10)

game_over = False

guess = input("Guess a number between 1 and 10 ")

while not game_over:
    guess = int(guess)
    if random_num < guess:
        guess = input("Too high, try again! ")
    elif random_num > guess:
        guess = input("Too low, try again! ")
    else:
        print(f"Correct! The number was {random_num}")
        again = input("Do you want to play again? (y/n) ")
        if again == "y":
             guess = input("Guess a number between 1 and 10 ")
        else:
            game_over = True



        
