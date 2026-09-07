"""
LeetCode 258 - Add Digits

Difficulty: Easy
Topic: Math, Digital Root

Problem Summary:
Given a non-negative integer, repeatedly add its digits until
only one digit remains.

Approach:
- Use the mathematical digital root property.
- If num is 0, return 0.
- If num is divisible by 9, return 9.
- Otherwise, return num % 9.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9


if __name__ == "__main__":
    obj = Solution()

    print(obj.addDigits(38))  # 2
    print(obj.addDigits(0))   # 0
    print(obj.addDigits(9))   # 9
