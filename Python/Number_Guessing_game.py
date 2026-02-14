import random

chosen = random.randint(1, 100)

print("Guess the number (between 1 and 100)!")

while True:
    guess = int(input("Enter your guess: "))

    if guess > chosen:
        print("Your guess is higher than the actual number.")
    elif guess < chosen:
        print("Your guess is lower than the actual number.")
    else:
        print("Great job! You guessed the correct number.")
        break