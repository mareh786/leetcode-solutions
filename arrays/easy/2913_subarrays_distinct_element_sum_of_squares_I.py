
"""
LeetCode 2913 - Subarrays Distinct Element Sum of Squares I

Difficulty: Easy
Topic: Array / Hash Set / Nested Loops

Problem Summary:
Given an integer array nums, consider every possible contiguous
subarray.

For each subarray:
- Count the number of distinct elements.
- Square that count.

Return the sum of the squared distinct-element counts for
all possible subarrays.

Approach:
Use two nested loops to generate every possible subarray.

Maintain a set to track distinct elements:
- The outer loop selects the starting index.
- Initialize an empty set for each starting index.
- The inner loop extends the subarray one element at a time.
- Add each element to the set.
- Calculate the number of distinct elements using len().
- Add the square of that count to total.

Finally, return total.

Time Complexity:
O(n^2)

Space Complexity:
O(n)
"""


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                total += count * count

        return total


if __name__ == "__main__":
    solution = Solution()

    print(solution.sumCounts([1, 2, 1]))  # 15
    print(solution.sumCounts([1, 1]))    # 3
