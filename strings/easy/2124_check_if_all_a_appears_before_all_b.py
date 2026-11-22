"""
LeetCode 2124 - Check if All A's Appears Before All B's

Difficulty: Easy
Topic: String

Problem Summary:
Given a string containing only 'a' and 'b',
check whether all occurrences of 'a' appear before
all occurrences of 'b'.

Approach:
1. Traverse the string starting from index 1.
2. Compare the current character with the previous character.
3. If the previous character is 'b' and the current character is 'a',
   return False.
4. If no such transition exists, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == "a" and s[i - 1] == "b":
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    print(solution.checkString("abab"))  # False
    print(solution.checkString("aaabbb"))  # True
    print(solution.checkString("aaa"))  # True
    print(solution.checkString("bbb"))  # True
    print(solution.checkString("aab"))  # True
