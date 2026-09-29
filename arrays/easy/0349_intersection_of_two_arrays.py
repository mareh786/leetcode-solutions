"""
LeetCode 349 - Intersection of Two Arrays

Difficulty: Easy
Topic: Hash Set

Problem Summary:
Given two integer arrays nums1 and nums2, return their intersection.
Each element in the result must be unique.

Approach:
Convert both arrays into sets and find their intersection.

Sets automatically remove duplicate values, and the '&' operator
returns the elements that are present in both sets.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)
"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    solution = Solution()

    print(solution.intersection([1, 2, 3], [2, 3, 4]))  # [2, 3]
