"""
LeetCode 372 - Super Pow

Difficulty: Medium
Topic: Math / Modular Exponentiation

Problem Summary:
Given an integer a and an array b representing a very large
integer, calculate a^b % 1337.

Approach:
1. Initialize mod = 1337 and res = 1.
2. Traverse each digit in b from left to right.
3. Update the result using:
   res = (res^10 * a^digit) % mod
4. Use Python's built-in pow(base, exp, mod) for
   efficient modular exponentiation.
5. Return the final result.

Time Complexity: O(n), where n is the number of digits in b.
Space Complexity: O(1)
"""


class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        mod = 1337
        res = 1

        for digit in b:
            res = (
                pow(res, 10, mod) *
                pow(a, digit, mod)
            ) % mod

        return res


if __name__ == "__main__":
    solution = Solution()

    print(solution.superPow(2, [1, 0]))    # 1024
    print(solution.superPow(2, [3]))      # 8
    print(solution.superPow(1, [4, 3]))   # 1
    print(solution.superPow(2147483647, [2, 0, 0]))  # 1198
