"""
LeetCode 69 - Sqrt(x)

Difficulty: Easy
Topic: Binary Search

Problem Summary:
Given a non-negative integer x, return the integer part of
the square root of x.

Approach:
- Use binary search between 0 and x.
- If mid * mid == x, mid is the answer.
- If mid * mid < x, mid could be the answer, so move right.
- If mid * mid > x, move left.
- Keep track of the largest valid mid in `ans`.

Time Complexity:
O(log x)

Space Complexity:
O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        while right >= left:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    obj = Solution()

    print(obj.mySqrt(4))   # 2
    print(obj.mySqrt(8))   # 2
    print(obj.mySqrt(0))   # 0
    print(obj.mySqrt(16))  # 4
