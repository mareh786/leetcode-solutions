"""
LeetCode 14 - Longest Common Prefix

Difficulty: Easy
Topic: Strings

Problem Summary:
Given an array of strings, find the longest common prefix shared
by all strings. Return an empty string if there is no common prefix.

Approach:
- Use the first string as the reference.
- Check each character of the first string against the same position
  in every other string.
- Stop as soon as a character differs or the index does not exist.
- Build and return the common prefix.

Time Complexity:
O(n * m)

Space Complexity:
O(m)

where:
- n = number of strings
- m = length of the shortest string.
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        # Iterate through each character of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # Check this character in all other strings
            for word in strs[1:]:

                # If index doesn't exist or character differs
                if i >= len(word) or word[i] != char:
                    return prefix

            # Character matched in all strings
            prefix += char

        return prefix


if __name__ == "__main__":
    obj = Solution()

    print(obj.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(obj.longestCommonPrefix(["dog", "racecar", "car"]))     # ""
    print(obj.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # "inters"
