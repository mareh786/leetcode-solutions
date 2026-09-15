"""
LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings

Difficulty: Hard
Topic: String, Palindrome, Greedy, Two Pointers

Problem Summary:
Given a string s and an integer k, find the maximum number of
non-overlapping palindromic substrings of length at least k.

Approach:
- Consider every possible odd and even palindrome center.
- Expand outward from each center.
- As soon as a palindrome of length at least k is found,
  select it if it does not overlap the previously selected
  palindrome.
- Take the smallest qualifying palindrome for each center
  to leave maximum space for future palindromes.

Time Complexity:
O(n^2)

Space Complexity:
O(1)
"""

from typing import *


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        last_end = 0
        count = 0

        for center in range(2 * n):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 >= k:
                    end = right + 1

                    if left >= last_end:
                        count += 1
                        last_end = end

                    break

                left -= 1
                right += 1

        return count
