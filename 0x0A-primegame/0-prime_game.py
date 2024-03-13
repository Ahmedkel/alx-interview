#!/usr/bin/python3
""" Prime Game. """


def get_primes(n):
    """List of primes up to n."""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return primes


def isWinner(x, nums):
    """ Determine the winner of the game. """
    if not x or not nums:
        return None
    maria_count = ben_count = 0
    for num in nums[:x]:
        primes = get_primes(num)
        if len(primes) % 2 == 0:
            ben_count += 1
        else:
            maria_count += 1
    if maria_count > ben_count:
        return 'Maria'
    elif ben_count > maria_count:
        return 'Ben'
    return None
