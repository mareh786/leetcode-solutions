"""
LeetCode 1401 - Circle and Rectangle Overlapping

Difficulty: Medium
Topic: Geometry, Math

Problem Summary:
Given a circle and an axis-aligned rectangle, determine whether
the circle and rectangle overlap.

Approach:
- Find the closest point on the rectangle to the center of
  the circle using coordinate clamping.
- Calculate the squared distance between the circle's center
  and this closest point.
- If the squared distance is less than or equal to the
  squared radius, the circle overlaps the rectangle.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""

class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int
    ) -> bool:

        # Find the closest point on the rectangle to the circle's center
        closest_x = min(max(xCenter, x1), x2)
        closest_y = min(max(yCenter, y1), y2)

        # Calculate squared distance
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        distance_squared = dx * dx + dy * dy

        return distance_squared <= radius * radius


if __name__ == "__main__":
    solution = Solution()

    print(
        solution.checkOverlap(
            radius=1,
            xCenter=0,
            yCenter=0,
            x1=1,
            y1=-1,
            x2=3,
            y2=1
        )
    )  # True
