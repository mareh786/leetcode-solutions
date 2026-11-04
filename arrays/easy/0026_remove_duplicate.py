"""
LeetCode 26 - Remove Duplicates from Sorted Array

Difficulty: Easy
Topic: Array / Two Pointers

Problem Summary:
Given a sorted array, remove duplicates in-place so that each
element appears only once. Return the number of unique elements.

Approach:
1. Handle the empty array separately.
2. Initialize j = 1 to track the position for the next unique element.
3. Traverse the array starting from index 1.
4. Compare the current element with the previous element.
5. If they are different:
   - Place the current element at index j.
   - Increment j.
6. Return j as the number of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)

    print(k)         # 5
    print(nums[:k])  # [0, 1, 2, 3, 4]
