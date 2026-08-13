"""
LeetCode Problem: 3731 - Find Missing Numbers
Difficulty: Easy

Approach:
- Find the minimum and maximum values in the list.
- Iterate through the range between them.
- Check whether each number exists in the input list.
- If not, add it to the result list.

Time Complexity:
O(n²)
(Checking `num in nums` takes O(n) for each element in the range.)

Space Complexity:
O(k)
where k is the number of missing elements.
"""


class Solution:
    def findMissingElements(self, nums):
        return [
            num
            for num in range(min(nums), max(nums))
            if num not in nums
        ]


if __name__ == "__main__":
    obj = Solution()

    print(obj.findMissingElements([5, 1]))        # [2, 3, 4]
    print(obj.findMissingElements([1, 4, 2, 5]))  # [3]
    print(obj.findMissingElements([7, 8, 6, 9]))  # []
