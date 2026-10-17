
"""
LeetCode 238 - Product of Array Except Self

Difficulty: Medium
Topic: Array / Prefix and Suffix Products

Problem Summary:
Given an integer array nums, return an array answer such that
answer[i] equals the product of all elements of nums except
nums[i].

The solution must run in O(n) time and must not use division.

Approach:
Use two passes with prefix and suffix products.

Initialize:
- ans: An array of length n.
- prefix_product: Product of all elements before the current index.
- suffix_product: Product of all elements after the current index.

First Pass (Left to Right):
- Store prefix_product in ans[i].
- Multiply prefix_product by nums[i].

Second Pass (Right to Left):
- Multiply ans[i] by suffix_product.
- Multiply suffix_product by nums[i].

Each position now contains the product of all elements
except the element at that position.

Time Complexity:
O(n)

Space Complexity:
O(1) auxiliary space, excluding the output array.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n

        prefix_product = 1
        suffix_product = 1

        for i in range(n):
            ans[i] = prefix_product
            prefix_product *= nums[i]

        for i in range(n - 1, -1, -1):
            ans[i] *= suffix_product
            suffix_product *= nums[i]

        return ans


if __name__ == "__main__":
    solution = Solution()

    print(solution.productExceptSelf([1, 2, 3, 4]))
    # [24, 12, 8, 6]

    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
    # [0, 0, 9, 0, 0]
