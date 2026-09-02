
"""
LeetCode 179 - Largest Number

Difficulty: Medium
Topic: Arrays, Sorting, Greedy

Problem Summary:
Given a list of non-negative integers, arrange them such that
they form the largest possible number.

Approach:
- Convert all numbers to strings.
- Compare two numbers a and b by checking:
      a + b
      b + a
- If b + a is larger, place b before a.
- Sort all numbers according to this custom comparison.
- Join the resulting strings.
- Handle cases where all numbers are zero.

Time Complexity:
O(n² * k)

Space Complexity:
O(n * k)

where k is the maximum number of digits.
"""

from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))

        for i in range(len(nums_str)):
            for j in range(i + 1, len(nums_str)):

                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]

        result = "".join(nums_str)

        if result[0] == "0":
            return "0"

        return result


if __name__ == "__main__":
    obj = Solution()

    print(obj.largestNumber([10, 2]))          # "210"
    print(obj.largestNumber([3, 30, 34, 5, 9])) # "9534330"
    print(obj.largestNumber([0, 0]))           # "0"
