# Lesson 9a - Project: Sieve of Eratosthenes
# Find every prime number from 1 to 1,000,000 and save them to primes.txt.
# Run this script with:  python3 sieve.py

import time


def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers from 2 up to and including limit."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for n in range(2, limit + 1):
        if is_prime[n]:
            # Any multiple of n below n*n was already crossed out by a
            # smaller prime, so start crossing out from n*n.
            for multiple in range(n * n, limit + 1, n):
                is_prime[multiple] = False

    return [n for n in range(2, limit + 1) if is_prime[n]]


def save_primes(primes, filename):
    """Write each prime to filename, one number per line."""
    with open(filename, "w") as f:
        for prime in primes:
            f.write(f"{prime}\n")


if __name__ == "__main__":
    limit = 1_000_000

    start = time.perf_counter()
    primes = sieve_of_eratosthenes(limit)
    save_primes(primes, "primes.txt")
    elapsed = time.perf_counter() - start

    print(f"Found {len(primes)} primes up to {limit:,}.")
    print(f"Saved to primes.txt in {elapsed:.2f} seconds.")
