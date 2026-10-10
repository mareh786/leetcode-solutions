
"""
LeetCode 2333 - Minimum Sum of Squared Difference

Difficulty: Medium
Topic: Greedy / Array / Frequency Counting

Problem Summary:
Given two integer arrays nums1 and nums2 of equal length,
and two integers k1 and k2, reduce elements in either array
by 1 per operation.

Perform at most k1 + k2 operations to minimize the sum of
squared differences between corresponding elements.

Approach:
First, calculate the absolute difference between each pair
of corresponding elements.

Let k = k1 + k2 represent the total available operations.

- If k is greater than or equal to the sum of all differences,
  every difference can be reduced to zero. Return 0.
- Find the maximum difference.
- Create a frequency array to count how many times each
  difference occurs.
- Traverse differences from largest to smallest.
- Reduce the largest differences first, moving their counts
  to the next smaller difference.
- Stop when all operations are used or no differences remain.

Reducing the largest differences first minimizes the sum
of squared differences.

Finally, calculate the sum of each squared difference
multiplied by its frequency.

Time Complexity:
O(n + m)

Space Complexity:
O(m)

Where:
n = length of nums1 and nums2
m = maximum absolute difference
"""


class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:
        diffs = [
            abs(nums1[i] - nums2[i])
            for i in range(len(nums1))
        ]

        k = k1 + k2
        total_diff = sum(diffs)

        if k >= total_diff:
            return 0

        max_diff = max(diffs)

        counts = [0] * (max_diff + 1)

        for d in diffs:
            counts[d] += 1

        for i in range(max_diff, 0, -1):
            if counts[i] == 0:
                continue

            reduce_amount = min(counts[i], k)

            counts[i] -= reduce_amount
            counts[i - 1] += reduce_amount

            k -= reduce_amount

            if k == 0:
                break

        return sum(
            counts[i] * (i * i)
            for i in range(max_diff + 1)
        )


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 4]
    nums2 = [2, 10, 20, 19]

    print(solution.minSumSquareDiff(nums1, nums2, 0, 0))
    # 579

    print(
        solution.minSumSquareDiff(
            [1, 2, 3, 4],
            [2, 10, 20, 19],
            1,
            2
        )
    )
    # 485
