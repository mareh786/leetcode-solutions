"""
LeetCode 8 - String to Integer (atoi)

Difficulty: Medium
Topic: Strings

Problem Summary:
Convert a string to a 32-bit signed integer by:
- Ignoring leading whitespace.
- Reading an optional '+' or '-' sign.
- Parsing consecutive digits.
- Stopping at the first non-digit character.
- Clamping the result to the 32-bit signed integer range.

Approach:
1. Remove leading and trailing whitespace.
2. Determine the sign if present.
3. Iterate through the string and build the integer digit by digit.
4. Stop parsing when a non-digit is encountered.
5. Apply the sign.
6. Clamp the value to the 32-bit signed integer range.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0

        s = s.strip()

        if not s:
            return 0

        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                sign = -1
            s = s[1:]

        for ch in s:
            if not ch.isdigit():
                break
            result = result * 10 + int(ch)

        value = sign * result

        if value > 2**31 - 1:
            return 2**31 - 1
        elif value < -2**31:
            return -2**31

        return value


if __name__ == "__main__":
    obj = Solution()

    print(obj.myAtoi("42"))             # 42
    print(obj.myAtoi("   -42"))         # -42
    print(obj.myAtoi("4193 with words"))# 4193
    print(obj.myAtoi("words and 987"))  # 0
    print(obj.myAtoi("-91283472332"))   # -2147483648
