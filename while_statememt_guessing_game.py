## Guessing game
## If you guess the right number(9 is here),
## you won. Otherwise you will died.
## You have three times. 

secret_number = 9

guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess:"))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("You lose!")

