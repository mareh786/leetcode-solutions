"""
LeetCode 856 - Score of Parentheses

Difficulty: Medium
Topic: String, Stack, Depth

Problem Summary:
Given a balanced parentheses string, calculate its score.

Rules:
- () has a score of 1.
- AB has a score of A + B.
- (A) has a score of 2 * A.

Approach:
Track the current nesting depth.

- When '(' is encountered, increase the depth.
- When ')' is encountered, decrease the depth.
- If the current ')' directly follows '(', it represents
  the primitive pair "()".
- Its score is 2 raised to the current depth.

This works because every level of nesting doubles the score.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1

            else:
                depth -= 1

                if s[i - 1] == "(":
                    score += 1 << depth

        return score


if __name__ == "__main__":
    solution = Solution()

    print(solution.scoreOfParentheses("()"))       # 1
    print(solution.scoreOfParentheses("(())"))     # 2
    print(solution.scoreOfParentheses("()()"))     # 2
    print(solution.scoreOfParentheses("(()())"))   # 4
