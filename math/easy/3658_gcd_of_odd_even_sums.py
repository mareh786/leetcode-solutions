"""
LeetCode 3658 - GCD of Odd and Even Sums

Difficulty: Easy
Topic: Math

Problem Summary:
Given n, calculate the sum of the first n positive odd numbers
and the first n positive even numbers, then return their GCD.

Observation:
Sum of the first n odd numbers = n²

Sum of the first n even numbers = n(n + 1)

Therefore:

gcd(n², n(n + 1))
= n * gcd(n, n + 1)
= n

Since consecutive numbers are always coprime,
gcd(n, n + 1) = 1.

So the answer is simply n.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n


if __name__ == "__main__":
    obj = Solution()

    print(obj.gcdOfOddEvenSums(4))  # 4
    print(obj.gcdOfOddEvenSums(5))  # 5
