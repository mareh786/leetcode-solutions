"""
LeetCode 242 - Valid Anagram

Difficulty: Easy
Topic: Strings, Sorting, Hash Table

Problem Summary:
Given two strings, determine whether one string is an anagram of the other.

Approach:
- Sort both strings.
- If the sorted strings are identical, they are anagrams.
- Otherwise, they are not.

Time Complexity:
O(n log n)

Space Complexity:
O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    obj = Solution()

    print(obj.isAnagram("anagram", "nagaram"))  # True
    print(obj.isAnagram("rat", "car"))          # False
