"""
LeetCode 342 - Power of Four

Difficulty: Easy
Topic: Math

Problem Summary:
Given an integer n, determine whether it is a power of four.

A number is a power of four if it can be written as:

    4^k

where k is a non-negative integer.

Approach:
- Return False for non-positive numbers.
- Continuously divide n by 4 while it is divisible by 4.
- If the value reaches 1, n is a power of four.
- If a value is not divisible by 4 before reaching 1,
  n is not a power of four.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 4 == 0:
                n //= 4
            else:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPowerOfFour(16))  # True
    print(solution.isPowerOfFour(8))   # False
    print(solution.isPowerOfFour(1))   # True
