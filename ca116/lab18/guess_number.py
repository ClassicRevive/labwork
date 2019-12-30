#!/usr/bin/env python


import secret_number

n = 1000

def play():
    guesses = 0
    low = 0
    mid = 500
    high = 1000

    new_guess = secret_number.guess(mid)
    while guesses < 10 and new_guess != "correct":
        # print new_guess
        if new_guess == "too-low":
            low = mid
        elif new_guess == "too-high":
            high = mid

        mid = (high + low) / 2
        new_guess = secret_number.guess(mid)

        guesses += 1

# testing
if __name__ == "__main__":
    play()
