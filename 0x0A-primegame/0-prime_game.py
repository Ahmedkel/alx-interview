#!/usr/bin/python3
""" Prime Game. """


def isWinner(x, nums):
    """ Determine the winner of the game. """
    maria_wins = 0
    ben_wins = 0

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_multiples(num, nums):
        """ Remove multiples of a number from a list. """
        return [n for n in nums if n % num != 0]

    for n in nums:
        if is_prime(n):
            while True:
                # Maria's turn
                if n in nums:
                    nums = remove_multiples(n, nums)
                    n = next((x for x in nums if is_prime(x)), None)
                    if n is None:
                        maria_wins += 1
                        break
                # Ben's turn
                else:
                    n = next((x for x in nums if is_prime(x)), None)
                    if n is None:
                        ben_wins += 1
                        break
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
