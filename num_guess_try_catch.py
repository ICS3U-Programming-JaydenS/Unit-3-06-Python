#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 28, 2025
# This programs is a number guessing game

import random


def main():

    # Gets the random number

    random_number = random.randint(1, 9)

    # Get the users guess and what to do if they dont pick a valid number

    try:
        user_guess = input("Guess a number between 1 and 9: ")
        user_guess_as_int = int(user_guess)

        if user_guess_as_int == random_number:
            print("You got it right!")
        elif user_guess_as_int != random_number:
            print("Wrong! It was", random_number, "!")

    except Exception:
        print("This is not a valid number!")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
