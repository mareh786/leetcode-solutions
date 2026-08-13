
"""
LeetCode 7 - Reverse Integer

Difficulty: Medium
Topic: Math

Problem Summary:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range,
return 0.

Approach:
1. Store the sign of the integer.
2. Convert the number to its absolute value.
3. Reverse the digits using string slicing.
4. Restore the original sign.
5. Check whether the reversed integer lies within the 32-bit signed integer range.

Time Complexity:
O(d)

Space Complexity:
O(d)

where d is the number of digits.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = int(str(x)[::-1]) * sign

        if -2**31 <= rev <= 2**31 - 1:
            return rev

        return 0


if __name__ == "__main__":
    obj = Solution()

    print(obj.reverse(123))          # 321
    print(obj.reverse(-123))         # -321
    print(obj.reverse(120))          # 21
    print(obj.reverse(1534236469))   # 0
