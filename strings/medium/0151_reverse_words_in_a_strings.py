"""
LeetCode 151 - Reverse Words in a String

Difficulty: Medium
Topic: Strings

Problem Summary:
Given a string containing words separated by spaces, reverse
the order of the words.

The returned string should:
- Remove leading and trailing spaces.
- Reduce multiple spaces between words to a single space.

Approach:
- Use split() to extract words from the string.
- Reverse the list of words using slicing.
- Join the reversed words with a single space.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split()
        reversed_s = " ".join(list_of_words[::-1])

        return reversed_s


if __name__ == "__main__":
    obj = Solution()

    print(obj.reverseWords("the sky is blue"))
    # "blue is sky the"

    print(obj.reverseWords("  hello world  "))
    # "world hello"

    print(obj.reverseWords("a good   example"))
    # "example good a"
