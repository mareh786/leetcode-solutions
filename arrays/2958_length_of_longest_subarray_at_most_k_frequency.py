"""
LeetCode 2958 - Length of Longest Subarray With at Most K Frequency

Difficulty: Medium
Topic: Arrays, Hash Map, Sliding Window

Problem Summary:
Find the length of the longest contiguous subarray in which
every element appears at most k times.

Approach:
- Use a sliding window with two pointers, i and j.
- `j` expands the window by adding elements.
- `seen` stores the frequency of each element.
- If the frequency of the current element exceeds k,
  move `i` forward until the window becomes valid again.
- Track the maximum valid window length.

Time Complexity:
O(n)

Space Complexity:
O(n)
"""

def maxSubarrayLength(nums, k):
    max_length = 0
    seen = {}
    i = 0

    for j in range(len(nums)):
        seen[nums[j]] = seen.get(nums[j], 0) + 1

        while seen[nums[j]] > k:
            seen[nums[i]] -= 1
            i += 1

        max_length = max(max_length, j - i + 1)

    return max_length


if __name__ == "__main__":
    print(maxSubarrayLength([1, 2, 1, 2, 1, 3, 4], 2))
    # 6
