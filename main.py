import random

number_of_guesses = 1
number = random.randint(1,50)


while True:
    user_choice = int(input("Choose a number between 1 and 50: "))
    if user_choice < number:
        print("That's below the target")
        number_of_guesses+=1
    elif user_choice > number:
        print("That's above the target")
        number_of_guesses+=1
    else:
        print(f"Correct! You guessed it in {number_of_guesses} attempts")
        break
