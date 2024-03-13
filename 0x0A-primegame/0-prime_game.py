#!/usr/bin/python3
""" Prime Game. """


def isWinner(x, nums):
    """ Determine the winner of the game. """
    maria_wins = 0
    ben_wins = 0

    def is_prime(n):
        """ Determine if a number is prime. """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_multiples(num, nums):
        """ Remove multiples of a number from a list. """
        new_nums = []
        for n in nums:
            if n % num != 0:
                new_nums.append(n)
        return new_nums

    for _ in range(x):
        maria_turn = True
        while nums:
            primes = [n for n in nums if is_prime(n)]
            if not primes:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            chosen_prime = max(
                primes, key=lambda n: len(remove_multiples(n, nums)))
            nums = remove_multiples(chosen_prime, nums)
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
