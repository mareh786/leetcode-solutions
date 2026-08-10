"""
LeetCode 88 - Merge Sorted Array

Difficulty: Easy
Topic: Arrays, Two Pointers

Problem Summary:
Merge two sorted arrays into nums1 in non-decreasing order.
nums1 has enough space to hold all elements from nums2.

Approach:
- Start from the end of both valid portions of nums1 and nums2.
- Compare the largest remaining elements.
- Place the larger element at the end of nums1.
- Continue until all elements from nums2 have been placed.

Working from the end prevents overwriting elements that
still need to be compared.

Time Complexity:
O(m + n)

Space Complexity:
O(1)
"""


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        i, j = m - 1, n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    obj.merge(nums1, 3, nums2, 3)
    print(nums1)  # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    nums2 = []

    obj.merge(nums1, 1, nums2, 0)
    print(nums1)  # [1]
