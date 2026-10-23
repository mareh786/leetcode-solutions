"""
LeetCode 796 - Rotate String

Difficulty: Easy
Topic: String

Problem Summary:
Given two strings s and goal, return True if goal can be
obtained by rotating s any number of times.

A rotation moves some characters from the beginning of s
to its end while preserving their order.

Approach:
First, check whether s and goal have the same length.
If their lengths differ, return False.

Otherwise, concatenate s with itself to create s + s.

Every possible rotation of s appears as a substring of s + s.

- If goal exists in s + s, return True.
- Otherwise, return False.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return goal in s + s


if __name__ == "__main__":
    solution = Solution()

    print(solution.rotateString("abc", "bca"))  # True
    print(solution.rotateString("abc", "acb"))  # False
    print(solution.rotateString("abc", "abc"))  # True
    print(solution.rotateString("abc", "abcd")) # False
