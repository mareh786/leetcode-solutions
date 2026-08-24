"""
LeetCode 35 - Search Insert Position

Difficulty: Easy
Topic: Binary Search

Problem Summary:
Given a sorted array of distinct integers and a target value,
return the index if the target is found. Otherwise, return the
index where the target should be inserted to maintain sorted order.

Approach:
- Use binary search to find the target.
- If the target is found, return its index.
- If the target is not found, `left` will eventually point to
  the correct insertion position.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    obj = Solution()

    print(obj.searchInsert([1, 3, 5, 6], 5))  # 2
    print(obj.searchInsert([1, 3, 5, 6], 2))  # 1
    print(obj.searchInsert([1, 3, 5, 6], 7))  # 4
    print(obj.searchInsert([1, 3, 5, 6], 0))  # 0
