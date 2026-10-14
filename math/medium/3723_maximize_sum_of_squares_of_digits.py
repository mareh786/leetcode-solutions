"""
LeetCode 3723 - Maximize Sum of Squares of Digits

Difficulty: Medium
Topic: Greedy / Math / String

Problem Summary:
Given two integers num and sum, construct the largest possible
num-digit integer whose digits add up to sum.

Return the integer as a string. If no valid number can be
constructed, return an empty string.

Approach:
Use a greedy strategy to maximize the sum of squared digits.

- If sum is greater than num * 9, return an empty string because
  each digit can be at most 9.
- Initialize an empty list to store the digits.
- Repeat num times:
  - Choose the largest possible digit using min(9, sum).
  - Append the digit to the result.
  - Subtract the chosen digit from sum.
- If sum becomes zero, join the digits and return the result.
- Otherwise, return an empty string.

Placing larger digits first maximizes the sum of their squares.

Time Complexity:
O(num)

Space Complexity:
O(num)
"""


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        final_num = []

        if sum > num * 9:
            return ""

        for _ in range(num):
            digit = min(9, sum)
            final_num.append(str(digit))
            sum -= digit

        return "".join(final_num) if sum == 0 else ""


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxSumOfSquares(2, 3))   # "30"
    print(solution.maxSumOfSquares(3, 20))  # "992"
    print(solution.maxSumOfSquares(2, 20))  # "99"
    print(solution.maxSumOfSquares(2, 25))  # ""
