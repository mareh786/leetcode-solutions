
"""
LeetCode 3498 - Reverse Degree of a String

Difficulty: Easy
Topic: String, Math

Problem Summary:
Given a string consisting of lowercase English letters,
calculate its reverse degree.

The reverse alphabetical value of a character is:
a = 26, b = 25, ..., z = 1.

For each character, multiply its reverse alphabetical value
by its 1-based position in the string and return the sum.

Approach:
- Convert each character to its reverse alphabetical value
  using ASCII values.
- Multiply the value by its 1-based position.
- Add the result to the total.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for index, char in enumerate(s):
            reverse_value = 26 - (ord(char) - ord("a"))
            result += (index + 1) * reverse_value

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.reverseDegree("abc"))  # 148
