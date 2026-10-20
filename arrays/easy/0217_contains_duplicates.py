"""
LeetCode 217 - Contains Duplicate

Difficulty: Easy
Topic: Array / Hash Set

Problem Summary:
Given an integer array nums, return True if any value appears
at least twice in the array.

Return False if every element is distinct.

Approach:
Use a set to keep track of elements already visited.

For every element:
- Check whether it already exists in the set.
- If it exists, return True because a duplicate is found.
- Otherwise, add the element to the set.

If the loop finishes without finding a duplicate, return False.

A set provides O(1) average-time membership checks.

Time Complexity:
O(n) average

Space Complexity:
O(n)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


if __name__ == "__main__":
    solution = Solution()

    print(solution.containsDuplicate([1, 2, 3, 1]))  # True
    print(solution.containsDuplicate([1, 2, 3, 4]))  # False
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    # True
