"""
LeetCode 169 - Majority Element

Difficulty: Easy
Topic: Array / Hash Map / Boyer-Moore Voting Algorithm

Problem Summary:
Given an integer array nums, return the majority element.

The majority element is the element that appears more than
floor(n / 2) times, where n is the length of the array.

The problem guarantees that a majority element exists.

Approach:
Use the Boyer-Moore Voting Algorithm to find the majority
element in O(n) time and O(1) extra space.

Maintain two variables:
- target: The current candidate for the majority element.
- count: The candidate's vote balance.

For every element:
- If count is zero, select the current element as target.
- If the current element equals target, increment count.
- Otherwise, decrement count.

Different elements cancel each other's votes. Since the
majority element appears more than half the time, it remains
the final candidate.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        target = 0
        count = 0

        for num in nums:
            if count == 0:
                target = num

            if num == target:
                count += 1
            else:
                count -= 1

        return target


if __name__ == "__main__":
    solution = Solution()

    print(solution.majorityElement([1, 1, 2, 3, 4, 2, 1, 2, 2, 2, 2, 2]))
    # 2
