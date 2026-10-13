"""
LeetCode 3727 - Maximum Alternating Sum of Squares

Difficulty: Medium
Topic: Array / Sorting / Greedy

Problem Summary:
Given an integer array nums, maximize the alternating sum
of squares after rearranging its elements.

The alternating sum is calculated by adding the squares of
elements at even indices and subtracting the squares of
elements at odd indices.

Approach:
First, square every element in nums and sort the squares
in ascending order.

Let n be the length of the array.

- Calculate the sum of all squared values.
- Subtract twice the sum of the smallest n // 2 squares.

This effectively adds the larger squares and subtracts the
smaller squares to maximize the result.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        squares = sorted(x * x for x in nums)

        max_sum = sum(squares) - 2 * sum(squares[:n // 2])

        return max_sum


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxAlternatingSum([1, 2, 3]))
