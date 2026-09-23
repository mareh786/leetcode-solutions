"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array

Difficulty: Medium
Topic: Array, Binary Search

Problem Summary:
Given a sorted array of integers, find the starting and ending
position of a given target value.

Return [-1, -1] if the target is not present.

Approach:
- Perform one binary search to find the first occurrence.
- Perform another binary search to find the last occurrence.
- When the target is found, continue searching in the required
  direction instead of stopping immediately.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_first() -> int:
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    result = mid
                    right = mid - 1

            return result

        def find_last() -> int:
            left = 0
            right = len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    result = mid
                    left = mid + 1

            return result

        return [find_first(), find_last()]


if __name__ == "__main__":
    solution = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    print(solution.searchRange(nums, target))  # [3, 4]
