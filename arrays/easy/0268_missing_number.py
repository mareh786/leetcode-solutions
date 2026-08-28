"""
LeetCode 268 - Missing Number

Difficulty: Easy
Topic: Arrays, Math

Problem Summary:
Given an array containing n distinct numbers from the range [0, n],
return the only number in the range that is missing from the array.

Approach:
- The sum of all numbers from 0 to n is:
      n * (n + 1) // 2
- Calculate the expected sum.
- Subtract the actual sum of the elements.
- The difference is the missing number.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum


if __name__ == "__main__":
    obj = Solution()

    print(obj.missingNumber([3, 0, 1]))     # 2
    print(obj.missingNumber([0, 1]))        # 2
    print(obj.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
