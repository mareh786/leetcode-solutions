"""
LeetCode 678 - Valid Parenthesis String

Difficulty: Medium
Topic: Greedy

Problem Summary:
Given a string s containing '(', ')' and '*', determine if the
string can be made valid by treating '*' as '(', ')' or an empty string.

Approach:
Maintain two variables:
- low: Minimum possible number of unmatched '('.
- high: Maximum possible number of unmatched '('.

For every character:
- If it is '(', increase both low and high.
- If it is ')', decrease both low and high.
- If it is '*', it can act as '(', ')' or empty:
  - Decrease low.
  - Increase high.

If high becomes negative, there is no possible valid interpretation.

Since low cannot be negative, reset it to 0 after each character.

At the end:
- If low == 0, the string can be valid.
- Otherwise, it cannot be valid.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == "(":
                low += 1
                high += 1

            elif c == ")":
                low -= 1
                high -= 1

            else:
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0


if __name__ == "__main__":
    solution = Solution()

    print(solution.checkValidString("()"))       # True
    print(solution.checkValidString("(*)"))      # True
    print(solution.checkValidString("(*))"))     # True
    print(solution.checkValidString("(((*)"))    # False
