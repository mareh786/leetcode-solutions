
"""
LeetCode 125 - Valid Palindrome

Difficulty: Easy
Topic: Strings, Two Pointers

Problem Summary:
Determine whether a string is a palindrome after converting
uppercase letters to lowercase and ignoring non-alphanumeric
characters.

Approach:
1. Remove non-alphanumeric characters and convert the remaining
   characters to lowercase.
2. Use two pointers:
   - `left` starts from the beginning.
   - `right` starts from the end.
3. Compare characters while moving both pointers toward the center.
4. Return False if any pair doesn't match.
5. If all pairs match, return True.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    obj = Solution()

    print(obj.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(obj.isPalindrome("race a car"))                       # False
    print(obj.isPalindrome(" "))                                # True
