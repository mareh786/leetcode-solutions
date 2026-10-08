
"""
LeetCode 1021 - Remove Outermost Parentheses

Difficulty: Easy
Topic: String / Stack

Problem Summary:
Given a valid parentheses string, remove the outermost pair of
parentheses from every primitive valid parentheses substring.

Approach:
Maintain a variable `level` to track the current nesting depth.

For every character:
- When we encounter ')', decrease the level first.
- If level > 0 after decreasing, the ')' is not an outermost
  parenthesis, so add it to the result.
- When we encounter '(', increase the level.
- If level > 0 before increasing, the '(' is not an outermost
  parenthesis, so it should be added to the result.

This removes the first '(' and last ')' of every primitive
parentheses group.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level = 0
        result = []

        for ch in s:
            if ch == ")":
                level -= 1

                if level > 0:
                    result.append(ch)

            else:
                if level > 0:
                    result.append(ch)

                level += 1

        return "".join(result)


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeOuterParentheses("(()())(())"))  # ()()()
    print(solution.removeOuterParentheses("(()())"))      # ()()
    print(solution.removeOuterParentheses("()()"))        # ""
