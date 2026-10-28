"""
LeetCode 976 - Largest Perimeter Triangle

Difficulty: Easy
Topic: Array / Sorting / Greedy

Problem Summary:
Given an integer array nums representing side lengths,
return the largest possible perimeter of a triangle that
can be formed using three elements.

If no valid triangle can be formed, return 0.

Approach:
First, sort the array in ascending order.

Traverse the array from right to left, checking three
consecutive elements:
- nums[i - 2]: Smallest side.
- nums[i - 1]: Middle side.
- nums[i]: Largest side.

A valid triangle must satisfy the triangle inequality:
The sum of the two smaller sides must be greater than
the largest side.

If this condition holds, return the sum of the three sides.
Since we check the largest sides first, this gives the
maximum possible perimeter.

If no valid triangle is found, return 0.

Time Complexity:
O(n log n)

Space Complexity:
O(1) auxiliary space, excluding sorting implementation.
"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i] + nums[i - 1] + nums[i - 2]

        return 0


if __name__ == "__main__":
    solution = Solution()

    print(solution.largestPerimeter([2, 1, 2]))  # 5
    print(solution.largestPerimeter([1, 2, 1]))  # 0
    print(solution.largestPerimeter([3, 2, 3, 4]))  # 10
