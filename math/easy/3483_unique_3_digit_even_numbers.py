"""
LeetCode 3483 - Unique 3-Digit Even Numbers

Difficulty: Easy
Topic: Array, Brute Force, Set

Problem Summary:
Given an array of digits, form unique 3-digit even numbers
using three different indices.

A valid number:
- Must have exactly 3 digits.
- Cannot start with 0.
- Must end with an even digit.
- Each index can be used only once.

Approach:
Use three nested loops to select the hundreds, tens, and
units digits. Use a set to store the generated numbers,
which automatically removes duplicates.

Time Complexity:
O(n^3)

Space Complexity:
O(n^3)
"""

from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):

                    # Each digit must come from a different index
                    if i == j or i == k or j == k:
                        continue

                    # A 3-digit number cannot start with zero
                    if digits[i] == 0:
                        continue

                    # The last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    numbers.add(number)

        return len(numbers)
