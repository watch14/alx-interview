#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """list of prime numbers."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers


def count_prime_factors(n, primes):
    """count the prime numbers"""
    is_removed = [False] * (n + 1)
    count = 0
    for prime in primes:
        if prime > n:
            break
        if not is_removed[prime]:
            count += 1
            for multiple in range(prime, n + 1, prime):
                is_removed[multiple] = True
    return count


def isWinner(x, nums):
    """winner"""
    if x == 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_prime_factors(n, primes)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
