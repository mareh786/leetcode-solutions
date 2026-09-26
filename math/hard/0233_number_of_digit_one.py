"""
LeetCode 233 - Number of Digit One

Difficulty: Hard
Topic: Math, Digit Manipulation

Problem Summary:
Given an integer n, count the total number of digit 1 appearing
in all non-negative integers from 1 to n.

Approach:
For every decimal position, split n into three parts:

    higher | current | lower

Based on the current digit:
- current == 0:
    higher * position
- current == 1:
    higher * position + lower + 1
- current > 1:
    (higher + 1) * position

Process every decimal position until position > n.

Time Complexity:
O(log n)

Space Complexity:
O(1)
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        position = 1

        while position <= n:
            higher = n // (position * 10)
            current = (n // position) % 10
            lower = n % position

            if current == 0:
                count += higher * position

            elif current == 1:
                count += higher * position + lower + 1

            else:
                count += (higher + 1) * position

            position *= 10

        return count


if __name__ == "__main__":
    solution = Solution()

    print(solution.countDigitOne(234))  # 134
