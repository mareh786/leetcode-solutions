
"""
LeetCode 2778 - Sum of Squares of Special Elements

Difficulty: Easy
Topic: Array / Math

Problem Summary:
Given a 0-indexed integer array nums of length n, return the
sum of squares of all special elements.

An element nums[i] is special if n is divisible by (i + 1).

Approach:
First, calculate the length of the array n.

Use enumerate() with start=1 to get each element's
1-based index.

For every element:
- Check whether n is divisible by its index.
- If divisible, add the square of the element to the sum.

Return the final sum.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for i, num in enumerate(nums, start=1):
            if n % i == 0:
                total += num * num

        return total


if __name__ == "__main__":
    solution = Solution()

    print(solution.sumOfSquares([1, 2, 3, 4]))  # 21
    print(solution.sumOfSquares([2, 7, 1, 19, 18, 3]))  # 63
