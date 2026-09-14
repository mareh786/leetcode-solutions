"""
LeetCode 836 - Rectangle Overlap

Difficulty: Easy
Topic: Geometry

Problem Summary:
Given two axis-aligned rectangles, determine whether they
overlap with a positive area.

Each rectangle is represented as:
[x1, y1, x2, y2]

where:
- (x1, y1) is the bottom-left corner.
- (x2, y2) is the top-right corner.

Approach:
Calculate the width and height of the overlapping region.

The rectangles overlap only when both dimensions are greater
than zero.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def isRectangleOverlap(
        self,
        rec1: List[int],
        rec2: List[int]
    ) -> bool:

        overlap_width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        overlap_height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])

        return overlap_width > 0 and overlap_height > 0


if __name__ == "__main__":
    solution = Solution()

    rec1 = [0, 0, 1, 1]
    rec2 = [2, 2, 3, 3]

    print(solution.isRectangleOverlap(rec1, rec2))  # False
