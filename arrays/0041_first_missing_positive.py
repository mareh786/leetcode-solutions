"""
LeetCode 41 - First Missing Positive

Difficulty: Hard
Topic: Arrays, Cyclic Sort

Problem Summary:
Find the smallest positive integer that does not appear in the array.

Approach:
- Every positive number x in the range [1, n] belongs at index x - 1.
- Rearrange the numbers so that each valid number is placed at its
  corresponding index.
- Ignore negative numbers, zero, and numbers greater than n.
- After rearranging, the first index i where nums[i] != i + 1
  identifies the smallest missing positive number.
- If every position is correct, the answer is n + 1.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number in its correct position
        for i in range(n):
            while (
                1 <= nums[i] <= n
                and nums[i] != nums[nums[i] - 1]
            ):
                correct_idx = nums[i] - 1

                nums[i], nums[correct_idx] = (
                    nums[correct_idx],
                    nums[i]
                )

        # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    obj = Solution()

    print(obj.firstMissingPositive([1, 2, 0]))       # 3
    print(obj.firstMissingPositive([3, 4, -1, 1]))   # 2
    print(obj.firstMissingPositive([7, 8, 9, 11, 12])) # 1
