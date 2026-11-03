"""
LeetCode 12 - Integer to Roman

Difficulty: Medium
Topic: String / Greedy

Problem Summary:
Convert an integer into its corresponding Roman numeral representation.

Approach:
1. Create a list of integer values and their corresponding Roman symbols.
2. Arrange the values in descending order.
3. Traverse the list and check how many times the current value fits into num.
4. Append the corresponding Roman symbol to the result.
5. Subtract the value from num each time it is used.
6. Return the final Roman numeral string.

Time Complexity: O(1) - For the fixed Roman numeral range (1 to 3999).
Space Complexity: O(1) - Excluding the output string.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        result = ""

        for value, sym in values:
            while num >= value:
                result += sym
                num -= value

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.intToRoman(19))    # XIX
    print(solution.intToRoman(58))    # LVIII
    print(solution.intToRoman(1994))  # MCMXCIV
    print(solution.intToRoman(3749))  # MMMDCCXLIX
