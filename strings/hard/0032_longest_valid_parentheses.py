"""
LeetCode 32 - Longest Valid Parentheses

Difficulty: Hard
Topic: String, Stack

Problem Summary:
Given a string containing only '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

Approach:
Use a stack to store indices.

- Start the stack with -1 as a base index.
- For an opening parenthesis, push its index.
- For a closing parenthesis, pop the most recent opening
  parenthesis index.
- If the stack becomes empty, push the current index as the
  new boundary.
- Otherwise, calculate the length of the current valid substring.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestValidParentheses("(()"))      # 2
    print(solution.longestValidParentheses(")()())"))   # 4
