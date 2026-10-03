"""
LeetCode 189 - Rotate Array

Difficulty: Medium
Topic: Array

Problem Summary:
Given an integer array nums, rotate the array to the right
by k steps.

Approach:
- Use k % n to handle cases where k is greater than the
  length of the array.
- Take the last k elements and place them before the remaining
  elements.
- Modify the original array using slice assignment.

For example:

    [1, 2, 3, 4, 5, 6, 7], k = 3

becomes:

    [5, 6, 7, 1, 2, 3, 4]

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        rotated = nums[-k:] + nums[:-k]
        nums[:] = rotated


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]

    solution.rotate(nums, 3)

    print(nums)  # [5, 6, 7, 1, 2, 3, 4]
