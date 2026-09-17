"""
LeetCode 1477 - Find Two Non-overlapping Sub-arrays Each With Target Sum

Difficulty: Medium
Topic: Array, Sliding Window, Prefix Minimum

Problem Summary:
Given an array of positive integers and a target value,
find two non-overlapping subarrays whose sums are equal to
target. Return the minimum sum of their lengths.

If no such pair exists, return -1.

Approach:
- Use a sliding window to find subarrays with sum == target.
- min_till[i] stores the minimum length of a valid subarray
  ending at or before index i.
- When a valid subarray [left, right] is found, combine its
  length with the shortest valid subarray ending before left.
- Keep the minimum combined length.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_till = [float("inf")] * (n + 1)

        left = 0
        window_sum = 0
        result = float("inf")

        for right, num in enumerate(arr):
            window_sum += num

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            current_len = right - left + 1

            if window_sum == target:
                if min_till[left] != float("inf"):
                    result = min(
                        result,
                        current_len + min_till[left]
                    )

                min_till[right + 1] = min(
                    min_till[right],
                    current_len
                )
            else:
                min_till[right + 1] = min_till[right]

        return -1 if result == float("inf") else result
