
"""
LeetCode 2567 - Minimum Score by Changing Two Elements

Difficulty: Medium
Topic: Array / Sorting / Greedy

Problem Summary:
Given an integer array nums, you can change any two elements
to any values.

Return the minimum possible difference between the maximum
and minimum elements after the changes.

Approach:
1. If the array has 3 or fewer elements, return 0.
2. Sort the array.
3. Consider the three possible ways to remove the influence
   of the extreme elements:
   - Change the 3 largest elements.
   - Change the 2 largest and 1 smallest elements.
   - Change the 1 largest and 2 smallest elements.
4. Calculate the remaining range for each case.
5. Return the minimum range.

Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space (excluding sorting).
"""


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        n = len(nums)

        if n <= 3:
            return 0

        nums.sort()

        ans1 = nums[n - 3] - nums[0]
        ans2 = nums[n - 2] - nums[1]
        ans3 = nums[n - 1] - nums[2]

        return min(ans1, ans2, ans3)


if __name__ == "__main__":
    solution = Solution()

    print(solution.minimizeSum([1, 4, 7, 8, 5]))  # 3
    print(solution.minimizeSum([1, 5, 6, 14, 15]))  # 1
    print(solution.minimizeSum([3, 100, 20]))  # 0
