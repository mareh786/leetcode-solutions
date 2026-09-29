"""
LeetCode 350 - Intersection of Two Arrays II

Difficulty: Easy
Topic: Sorting, Two Pointers

Problem Summary:
Given two integer arrays nums1 and nums2, return their intersection.
Each element may appear in the result as many times as it appears
in both arrays.

Approach:
1. Sort both arrays.
2. Use two pointers to compare elements.
3. If both elements are equal, add the element to the result
   and move both pointers.
4. If nums1[i] is smaller, move pointer i.
5. Otherwise, move pointer j.

Sorting allows us to efficiently compare the elements while
preserving duplicate occurrences.

Time Complexity:
O(n log n + m log m)

Space Complexity:
O(n + m)
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.intersect([1, 2, 3, 3, 4], [3, 3, 4]))  # [3, 3, 4]
