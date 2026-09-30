"""
LeetCode 442 - Find All Duplicates in an Array

Difficulty: Medium
Topic: Array, Hash Set

Problem Summary:
Given an integer array nums of length n where each integer is
in the range [1, n] and each integer appears once or twice,
return all integers that appear twice.

Approach:
Use a set to keep track of numbers that have already been seen.

For each number:
- If it is already in the set, it is a duplicate.
- Otherwise, add it to the set.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        result = []

        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # [2, 3]
    print(solution.findDuplicates([1]))  # []
