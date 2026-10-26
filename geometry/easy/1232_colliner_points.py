
"""
LeetCode 1232 - Check If It Is a Straight Line

Difficulty: Easy
Topic: Array / Math / Geometry

Problem Summary:
Given an array of coordinates, determine whether all points
lie on a single straight line.

Each coordinate is represented as [x, y].

Approach:
Take the first two points as the reference points:
- (x1, y1)
- (x2, y2)

For every point (x, y), check whether it lies on the same
straight line using the cross-product formula.

The condition is:

(y2 - y1) * (x1 - x) == (x2 - x1) * (y1 - y)

This avoids division, so vertical lines are handled correctly
without special cases.

If any point violates the condition, return False.
Otherwise, return True.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]

        for x, y in coordinates:
            if (y2 - y1) * (x1 - x) != (x2 - x1) * (y1 - y):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    print(solution.checkStraightLine(
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    ))  # True

    print(solution.checkStraightLine(
        [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    ))  # False
