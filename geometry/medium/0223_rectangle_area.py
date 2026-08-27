
"""
LeetCode 223 - Rectangle Area

Difficulty: Medium
Topic: Geometry, Math

Problem Summary:
Given the coordinates of two axis-aligned rectangles, calculate
the total area covered by the two rectangles.

If the rectangles overlap, the overlapping area should only be
counted once.

Approach:
1. Calculate the area of each rectangle.
2. Find the width of the overlapping region.
3. Find the height of the overlapping region.
4. Calculate the overlapping area.
5. Add both rectangle areas and subtract the overlap.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int
    ) -> int:

        # Area of Rectangle A
        area_A = (ax2 - ax1) * (ay2 - ay1)

        # Area of Rectangle B
        area_B = (bx2 - bx1) * (by2 - by1)

        # Find overlapping length
        overlap_length = min(ax2, bx2) - max(ax1, bx1)
        overlap_length = max(overlap_length, 0)

        # Find overlapping width
        overlap_width = min(ay2, by2) - max(ay1, by1)
        overlap_width = max(overlap_width, 0)

        # Calculate overlapping area
        overlap_area = overlap_length * overlap_width

        return area_A + area_B - overlap_area


if __name__ == "__main__":
    obj = Solution()

    print(obj.computeArea(
        -3, 0, 3, 4,
        0, -1, 9, 2
    ))  # 45
