
import random

secret_number = random.randint(1, 50)
lives = 5

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 50.")
print("You have 5 attempts to guess it.")

while lives > 0:
    guess = int(input("\nEnter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed correctly!")
        break
    elif guess < secret_number:
        print("Hint: Try a HIGHER number!")
    else:
        print("Hint: Try a LOWER number!")

    lives -= 1
    print("Lives remaining:", lives)

if lives == 0:
    print("Game over!")
    print("The secret number was:", secret_number)
