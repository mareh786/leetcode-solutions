"""
LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum

Difficulty: Easy
Topic: Arrays

Problem Summary:
Find the sum of the longest sequential prefix of nums.
Then return the smallest integer greater than or equal to that sum
that does not appear in nums.

Approach:
1. Start with the first element as the beginning of the sequential prefix.
2. Continue while each next element is exactly one greater than the previous.
3. Calculate the sum of this sequential prefix.
4. Starting from the prefix sum, increment the value while it exists in nums.
5. Return the first value that does not exist.

Time Complexity:
O(n²) in the worst case because `sum in nums` is O(n).

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        current = nums[0]
        total = current

        for i in range(1, len(nums)):
            if nums[i] == current + 1:
                current = nums[i]
                total += current
            else:
                break

        while total in nums:
            total += 1

        return total


if __name__ == "__main__":
    obj = Solution()

    print(obj.missingInteger([1, 2, 3, 2, 5]))  # 6
    print(obj.missingInteger([3, 4, 5, 1, 12])) # 18
