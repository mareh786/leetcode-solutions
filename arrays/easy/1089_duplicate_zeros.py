"""
LeetCode 1089 - Duplicate Zeros

Difficulty: Easy
Topic: Array / Two Pointers

Problem Summary:
Given a fixed-length integer array arr, duplicate each occurrence
of zero and shift the remaining elements to the right.

Elements beyond the original array length are discarded.

The modification must be done in-place.

Approach:
First, count the number of zeros in the array.

Use two pointers starting from the end:
- i: Points to the original elements.
- j: Represents the position where the element would go after
     accounting for duplicated zeros.

Process the array from right to left.

For each element:
- Copy arr[i] to arr[j] if j is inside the original array.
- If arr[i] is zero, place another zero at the previous position.
- Move both pointers backwards.

Processing from right to left prevents overwriting elements
that have not been processed yet.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)

        i = n - 1
        j = n + zeros - 1

        while i < j:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1

                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1


if __name__ == "__main__":
    solution = Solution()

    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(arr1)
    print(arr1)  # [1, 0, 0, 2, 3, 0, 0, 4]

    arr2 = [1, 2, 3]
    solution.duplicateZeros(arr2)
    print(arr2)  # [1, 2, 3]
