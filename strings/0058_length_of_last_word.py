"""
LeetCode 58 - Length of Last Word

Difficulty: Easy
Topic: Strings

Problem Summary:
Given a string consisting of words and spaces, return the length
of the last word in the string.

Approach:
1. Split the string into words.
2. Access the last word.
3. Return its length.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last_word = words[-1]
        return len(last_word)


if __name__ == "__main__":
    obj = Solution()

    print(obj.lengthOfLastWord("Hello World"))                # 5
    print(obj.lengthOfLastWord("   fly me   to   the moon"))  # 4
    print(obj.lengthOfLastWord("luffy is still joyboy"))      # 6
