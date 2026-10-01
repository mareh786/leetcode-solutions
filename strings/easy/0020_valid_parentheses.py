"""
LeetCode 20 - Valid Parentheses

Difficulty: Easy
Topic: String, Stack

Problem Summary:
Given a string containing only '(', ')', '{', '}', '[' and ']',
determine whether the brackets are valid.

A valid string must satisfy:
- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches its most recent opening bracket.

Approach:
Use a stack to store opening brackets.

For each character:
- If it is an opening bracket, push it onto the stack.
- If it is a closing bracket:
    - Return False if the stack is empty.
    - Pop the most recent opening bracket.
    - Check whether it matches the closing bracket.

At the end, the stack must be empty.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if (
                    (ch == ")" and top != "(")
                    or (ch == "}" and top != "{")
                    or (ch == "]" and top != "[")
                ):
                    return False

        return not stack


if __name__ == "__main__":
    solution = Solution()

    print(solution.isValid("()"))       # True
    print(solution.isValid("()[]{}"))   # True
    print(solution.isValid("(]"))       # False
    print(solution.isValid("([)]"))     # False
    print(solution.isValid("{[]}"))     # True
