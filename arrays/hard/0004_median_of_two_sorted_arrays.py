"""
LeetCode 4 - Median of Two Sorted Arrays

Difficulty: Hard
Topic: Arrays, Two Pointers, Binary Search

Problem Summary:
Given two sorted arrays, find the median of the combined
sorted elements.

Approach:
- Use two pointers to merge both sorted arrays.
- Compare elements from both arrays and append the smaller one.
- Append any remaining elements.
- Calculate the median of the merged array.

Time Complexity:
O(m + n)

Space Complexity:
O(m + n)
"""


from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        i = 0
        j = 0
        merged_nums = []

        # Merge both sorted arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        # Add remaining elements from nums1
        while i < len(nums1):
            merged_nums.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < len(nums2):
            merged_nums.append(nums2[j])
            j += 1

        # Calculate median
        n = len(merged_nums)

        if n % 2 == 1:
            return merged_nums[n // 2]

        return (
            merged_nums[n // 2 - 1]
            + merged_nums[n // 2]
        ) / 2


if __name__ == "__main__":
    obj = Solution()

    print(obj.findMedianSortedArrays([1, 3], [2]))       # 2.0
    print(obj.findMedianSortedArrays([1, 2], [3, 4]))    # 2.5
