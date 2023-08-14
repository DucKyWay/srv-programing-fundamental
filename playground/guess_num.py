import random

num = 0
ans = random.randint(1, 10)
guess = 8

name = input("Hello! What is your name? ")
print(name + ", I am thinking of a whole number between 1 and 10. Can you guess what it is?")

while num != ans:
    guess = input("Take a guess ")
    guess = int(guess)
    guessesLeft = 8 - num;

    if guess < ans:
        guessesLeft = str(guessesLeft)
        print("Your guess is too low! You have " + guessesLeft + " guesses left")
        num = num + 1;

    elif guess > ans:
        guessesLeft = str(guessesLeft)
        print("Your guess is too high! You have " + guessesLeft + " guesses left")
        num = num + 1;

    elif guessesLeft == 0:
        print("Sorry. The number I was thinking of was " + ans + "")
        num = num + 1;

    elif guess == ans:
        num = str(num)
        print("Good job! You guessed the number in " + num + " tries ")
        break

    if guessesLeft == 1:
        print("Sorry. The number I was thinking of was " + ans + "")
