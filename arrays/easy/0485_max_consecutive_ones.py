
"""
LeetCode 485 - Max Consecutive Ones

Difficulty: Easy
Topic: Array

Problem Summary:
Given a binary array nums, return the maximum number of
consecutive 1s in the array.

Approach:
Maintain two variables:
- current_count: Number of consecutive 1s ending at the
  current position.
- max_count: Maximum consecutive 1s found so far.

For every element:
- If it is 1, increase current_count and update max_count.
- If it is 0, reset current_count to 0.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0

        return max_count


if __name__ == "__main__":
    solution = Solution()

    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 3
    print(solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 2
