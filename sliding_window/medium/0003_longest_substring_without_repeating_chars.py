"""
LeetCode 3 - Longest Substring Without Repeating Characters

Difficulty: Medium
Topic: Strings, Hash Set, Sliding Window

Problem Summary:
Given a string, find the length of the longest substring
that contains no repeating characters.

Approach:
- Use a sliding window with two pointers.
- Maintain a set containing characters currently in the window.
- Expand the window using the right pointer.
- If a duplicate character is found, shrink the window from
  the left until the duplicate is removed.
- Track the maximum window length.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen_chars = set()

        for right in range(len(s)):

            # Remove characters until the duplicate is removed
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            # Add current character to the window
            seen_chars.add(s[right])

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    obj = Solution()

    print(obj.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(obj.lengthOfLongestSubstring("bbbbb"))     # 1
    print(obj.lengthOfLongestSubstring("pwwkew"))    # 3
    print(obj.lengthOfLongestSubstring(""))          # 0
