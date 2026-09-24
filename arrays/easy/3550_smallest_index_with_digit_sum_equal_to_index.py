
"""
LeetCode - Smallest Index With Equal Value to Digit Sum

Difficulty: Easy
Topic: Array, Math

Problem Summary:
Given an integer array, find the smallest index i such that
the sum of the digits of nums[i] is equal to i.

Return -1 if no such index exists.

Approach:
- Traverse the array from left to right.
- Calculate the digit sum of each number.
- Compare the digit sum with the current index.
- Return immediately when a match is found.

Time Complexity:
O(n * d)

where d is the number of digits in each number.

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            number = nums[i]
            digit_sum = 0

            while number > 0:
                digit_sum += number % 10
                number //= 10

            if digit_sum == i:
                return i

        return -1
