#!/usr/bin/python3
"""
A python script for determining a winner
"""


def isWinner(x, nums):
    """
    A function that determines the winner
    of each game.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    winner = 0
    for n in nums:
        if is_prime(n):
            winner = 1
        else:
            winner = 2

    return "Maria" if winner == 1 else "Ben" if winner == 2 else None
