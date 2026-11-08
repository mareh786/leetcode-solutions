"""
LeetCode 633 - Sum of Square Numbers

Difficulty: Medium
Topic: Math / Two Pointers

Problem Summary:
Given a non-negative integer c, determine whether there exist
two integers a and b such that:

a² + b² = c

Approach:
1. Initialize start = 0 and end = sqrt(c).
2. Use two pointers to check possible pairs.
3. Calculate start² + end².
4. If the sum equals c, return True.
5. If the sum is smaller than c, increment start.
6. If the sum is greater than c, decrement end.
7. If no valid pair is found, return False.

Time Complexity: O(sqrt(c))
Space Complexity: O(1)
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))

        while start <= end:
            total = start * start + end * end

            if total == c:
                return True
            elif total < c:
                start += 1
            else:
                end -= 1

        return False


if __name__ == "__main__":
    solution = Solution()

    print(solution.judgeSquareSum(6))   # False
    print(solution.judgeSquareSum(5))   # True (1² + 2²)
    print(solution.judgeSquareSum(25))  # True (0² + 5²)
    print(solution.judgeSquareSum(3))   # False
