"""
LeetCode 164 - Maximum Gap

Difficulty: Medium
Topic: Array / Sorting

Problem Summary:
Given an integer array nums, return the maximum difference
between two successive elements in its sorted form.

If the array contains fewer than two elements, return 0.

Approach:
First, check whether the array has fewer than two elements.
If so, return 0.

Sort the array in ascending order.

Initialize max_diff to 0 and compare each pair of adjacent
elements in the sorted array.

For every pair:
- Calculate the difference between the current element and
  the previous element.
- Update max_diff if the difference is larger.

Return max_diff.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        sorted_nums = sorted(nums)
        max_diff = 0

        for i in range(1, len(sorted_nums)):
            diff = sorted_nums[i] - sorted_nums[i - 1]
            max_diff = max(max_diff, diff)

        return max_diff


if __name__ == "__main__":
    solution = Solution()

    print(solution.maximumGap([3, 6, 9, 1]))  # 3
    print(solution.maximumGap([10]))          # 0
    print(solution.maximumGap([1, 10000000]))  # 9999999
