#!/usr/bin/env python3

import sys


def main():
    hierarchy = {"paper": "rock",
                 "rock": "scissors",
                 "scissors": "paper"}

    for line in sys.stdin:
        player1, player2 = line.strip().split()

        # win lose cases for players
        for k, v in hierarchy.items():
            if player1 == k and player2 == v:
                print("Player 1 wins")
            elif player2 == k and player1 == v:
                print("Player 2 wins")

        # draw case
        if player1 == player2:
                print("Draw")


if __name__ == '__main__':
    main()
