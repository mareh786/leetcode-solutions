
"""
LeetCode 50 - Pow(x, n)

Difficulty: Medium
Topic: Math, Recursion, Binary Exponentiation

Problem Summary:
Calculate x raised to the power n.

Approach:
- If n is 0, return 1.
- If n is negative, use the reciprocal of x and make n positive.
- Recursively calculate x^(n // 2).
- If n is even, square the result.
- If n is odd, multiply the result by x once more.

Time Complexity:
O(log n)

Space Complexity:
O(log n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half

        return x * half * half


if __name__ == "__main__":
    obj = Solution()

    print(obj.myPow(2.0, 10))   # 1024.0
    print(obj.myPow(2.0, -2))   # 0.25
    print(obj.myPow(2.0, 0))    # 1
