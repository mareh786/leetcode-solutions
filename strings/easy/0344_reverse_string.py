"""
LeetCode 344 - Reverse String

Difficulty: Easy
Topic: Strings, Two Pointers

Problem Summary:
Reverse a list of characters in-place.

Approach:
- Use two pointers.
- One pointer starts from the beginning.
- Another pointer starts from the end.
- Swap characters and move both pointers toward the center.
- Continue until both pointers meet.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


if __name__ == "__main__":
    obj = Solution()

    chars = ["h", "e", "l", "l", "o"]
    obj.reverseString(chars)

    print(chars)  # ['o', 'l', 'l', 'e', 'h']
