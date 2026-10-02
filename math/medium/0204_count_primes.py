"""
LeetCode 204 - Count Primes

Difficulty: Medium
Topic: Math, Array, Number Theory

Problem Summary:
Given an integer n, return the number of prime numbers that
are strictly less than n.

Approach:
Use the Sieve of Eratosthenes.

- Initially assume every number from 2 to n - 1 is prime.
- For each prime number i, mark all of its multiples as
  non-prime.
- Start marking from i * i because smaller multiples have
  already been handled by smaller prime numbers.
- Count the remaining numbers marked as prime.

Time Complexity:
O(n log log n)

Space Complexity:
O(n)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return is_prime.count(True)


if __name__ == "__main__":
    solution = Solution()

    print(solution.countPrimes(10))  # 4
