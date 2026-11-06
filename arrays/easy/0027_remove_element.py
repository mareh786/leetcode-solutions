
"""
LeetCode 27 - Remove Element

Difficulty: Easy
Topic: Array / Two Pointers

Problem Summary:
Remove all occurrences of a given value from an array in-place.
Return the number of elements that are not equal to val.

Approach:
1. Initialize index = 0 to track the position for valid elements.
2. Traverse the array using i.
3. If nums[i] is not equal to val:
   - Copy nums[i] to nums[index].
   - Increment index.
4. Return index as the count of remaining elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 2]
    k = solution.removeElement(nums, 2)

    print(k)         # 2
    print(nums[:k])  # [1, 3]
