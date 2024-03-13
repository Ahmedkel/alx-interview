#!/usr/bin/python3
""" Prime Game. """


def isWinner(x, nums):
    """ Determine the winner of the game. """
    maria_wins = 0
    ben_wins = 0


    def is_prime(n):
        """ Check if a number is prime. """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


    for _ in range(x):

        primes = [num for num in nums if is_prime(num)]
        if not primes:
            return None


        chosen_prime = max(primes)

        nums = [num for num in nums if num != chosen_prime and num % chosen_prime != 0]


        if _ % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1


    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
