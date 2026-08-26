
"""
LeetCode 205 - Isomorphic Strings

Difficulty: Easy
Topic: Strings, Hash Table

Problem Summary:
Determine whether two strings are isomorphic.

Two strings are isomorphic if the characters in one string can be
replaced to obtain the other string while maintaining the same
character mapping throughout.

Approach:
- Use two dictionaries to maintain mappings in both directions.
- map_s_t maps characters from s to t.
- map_t_s maps characters from t to s.
- If an existing mapping conflicts in either direction, return False.
- If all characters maintain a consistent one-to-one mapping, return True.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

from typing import *


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
            if (
                (c1 in map_s_t and map_s_t[c1] != c2)
                or
                (c2 in map_t_s and map_t_s[c2] != c1)
            ):
                return False

            map_s_t[c1] = c2
            map_t_s[c2] = c1

        return True


if __name__ == "__main__":
    obj = Solution()

    print(obj.isIsomorphic("egg", "add"))    # True
    print(obj.isIsomorphic("foo", "bar"))    # False
    print(obj.isIsomorphic("paper", "title"))  # True
    print(obj.isIsomorphic("badc", "baba"))  # False
