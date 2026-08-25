"""
LeetCode 3718 - Smallest Missing Multiple of K

Difficulty: Easy
Topic: Arrays, Hash Set

Problem Summary:
Given an integer array nums and an integer k, find the smallest
positive multiple of k that does not exist in nums.

Approach:
- Convert nums into a set for fast membership checking.
- Start with k, the smallest positive multiple.
- Keep increasing by k while the current multiple exists.
- Return the first multiple that is not present.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)

        multiple = k

        while multiple in num_set:
            multiple += k

        return multiple


if __name__ == "__main__":
    obj = Solution()

    print(obj.missingMultiple([8, 2, 3, 4, 6], 2))  # 10
    print(obj.missingMultiple([1, 4, 7, 10], 3))     # 3
