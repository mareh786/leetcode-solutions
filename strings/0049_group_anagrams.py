"""
LeetCode 49 - Group Anagrams

Difficulty: Medium
Topic: Strings, Hash Table

Problem Summary:
Group together all strings that are anagrams of each other and return the groups.

Approach:
- Sort each string alphabetically.
- Use the sorted string as the key in a dictionary.
- Append the original string to the corresponding list.
- Return all grouped values.

Time Complexity:
O(n * k log k)
where:
- n = number of strings
- k = maximum length of a string

Space Complexity:
O(n * k)
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    obj = Solution()

    print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
