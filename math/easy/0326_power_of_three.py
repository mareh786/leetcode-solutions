"""
LeetCode 326 - Power of Three

Difficulty: Easy
Topic: Math

Problem Summary:
Given an integer n, return True if n is a power of three.
Otherwise, return False.

A number is a power of three if it can be written as:

3^k

where k is a non-negative integer.

Approach:
First, check if n is less than or equal to 0.
If so, it cannot be a power of three.

Then repeatedly divide n by 3 while it is completely
divisible by 3.

If n becomes 1, the original number was a power of three.
Otherwise, it was not.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPowerOfThree(27))  # True
    print(solution.isPowerOfThree(45))  # False
    print(solution.isPowerOfThree(1))   # True
