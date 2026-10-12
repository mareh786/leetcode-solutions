"""
LeetCode 643 - Maximum Average Subarray I

Difficulty: Easy
Topic: Array / Sliding Window

Problem Summary:
Given an integer array nums and an integer k, find the
contiguous subarray of length k that has the maximum average.

Return the maximum average value.

Approach:
Use the sliding window technique to avoid recalculating
the sum of every subarray.

- Calculate the sum of the first k elements.
- Initialize max_sum with the initial window sum.
- Slide the window one element at a time:
  - Add the new element entering the window.
  - Subtract the element leaving the window.
  - Update max_sum if the current window sum is greater.
- Return max_sum divided by k.

This improves the brute-force approach by reusing the
previous window's sum.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    print(solution.findMaxAverage(nums, k))  # 12.75
