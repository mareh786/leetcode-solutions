
"""
LeetCode 136 - Single Number

Difficulty: Easy
Topic: Bit Manipulation, XOR

Problem Summary:
Given an integer array where every element appears twice except
for one element, find the element that appears only once.

Approach:
- XOR all elements together.
- XOR has two important properties:
    1. a ^ a = 0
    2. a ^ 0 = a
- Therefore, duplicate numbers cancel each other out.
- The remaining value is the number that appears once.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


if __name__ == "__main__":
    obj = Solution()

    print(obj.singleNumber([2, 2, 1]))        # 1
    print(obj.singleNumber([4, 1, 2, 1, 2]))  # 4
    print(obj.singleNumber([1]))              # 1
