import random

number_to_guess = random.randint (1,100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < number_to_guess:
            print("too low")
        elif guess > number_to_guess:
            print("too high")
        else:
            print("Yes! you found the number")
            break

    except ValueError:
        print ("Please enter a valid number")

