"""
LeetCode 283 - Move Zeroes

Difficulty: Easy
Topic: Array, Two Pointers

Problem Summary:
Move all zeroes to the end of the array while maintaining
the relative order of the non-zero elements.

The operation must be performed in-place.

Approach:
- Use a pointer to track the position where the next non-zero
  element should be placed.
- Traverse the array and swap each non-zero element into that
  position.
- All remaining positions naturally contain zeroes.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        insert_position = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_position], nums[i] = (
                    nums[i],
                    nums[insert_position]
                )
                insert_position += 1


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 13, 3, 0, 2]
    solution.moveZeroes(nums)

    print(nums)  # [13, 3, 2, 0, 0]
