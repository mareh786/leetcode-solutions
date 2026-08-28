"""
LeetCode 263 - Ugly Number

Difficulty: Easy
Topic: Math

Problem Summary:
An ugly number is a positive integer whose prime factors are
limited to 2, 3, and 5.

Return True if n is an ugly number; otherwise return False.

Approach:
- Reject non-positive numbers.
- Repeatedly divide n by 2, 3, or 5 whenever possible.
- If n cannot be divided by any of these numbers and is still
  greater than 1, it contains another prime factor.
- If n becomes 1, it is an ugly number.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    print(obj.isUgly(6))    # True
    print(obj.isUgly(1))    # True
    print(obj.isUgly(14))   # False
    print(obj.isUgly(0))    # False
