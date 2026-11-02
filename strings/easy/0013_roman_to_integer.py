"""
LeetCode 13 - Roman to Integer

Difficulty: Easy
Topic: Hash Map / String

Problem Summary:
Convert a Roman numeral string into its corresponding integer.

Approach:
1. Create a dictionary mapping each Roman symbol to its integer value.
2. Traverse the string from left to right.
3. If the current symbol has a smaller value than the next symbol,
   subtract its value from the total.
4. Otherwise, add its value to the total.
5. Return the final total.

Time Complexity: O(n)
Space Complexity: O(1) - Fixed-size dictionary.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total


if __name__ == "__main__":
    solution = Solution()

    print(solution.romanToInt("IV"))       # 4
    print(solution.romanToInt("III"))      # 3
    print(solution.romanToInt("LVIII"))    # 58
    print(solution.romanToInt("MCMXCIV"))  # 1994
