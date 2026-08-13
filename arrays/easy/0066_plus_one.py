"""
LeetCode 66 - Plus One

Difficulty: Easy
Topic: Arrays, Math

Problem Summary:
Given an array of digits representing a non-negative integer,
increment the integer by one and return the resulting digits.

Approach:
- Convert the digit array into an integer.
- Add one to the integer.
- Convert the result back into a list of digits.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for digit in digits:
            num = num * 10 + digit

        final_result = num + 1

        return [int(digit) for digit in str(final_result)]


if __name__ == "__main__":
    obj = Solution()

    print(obj.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(obj.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(obj.plusOne([9]))  # [1, 0]
