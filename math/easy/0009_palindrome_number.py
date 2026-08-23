
"""
LeetCode 9 - Palindrome Number

Difficulty: Easy
Topic: Math

Problem Summary:
Given an integer x, determine whether it reads the same
forward and backward.

Approach:
- Store the original number.
- Reverse the digits mathematically.
- Compare the reversed number with the original number.
- Negative numbers are not palindromes.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed_num = 0

        if x < 0:
            return False

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


if __name__ == "__main__":
    obj = Solution()

    print(obj.isPalindrome(121))   # True
    print(obj.isPalindrome(-121))  # False
    print(obj.isPalindrome(10))    # False
    print(obj.isPalindrome(0))     # True
