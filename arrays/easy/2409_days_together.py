"""
LeetCode 2409 - Count Days Spent Together

Difficulty: Easy
Topic: String / Array / Date Calculation

Problem Summary:
Alice and Bob each have an arrival date and a departure date
in the format "MM-DD".

Return the number of days they spend together, counting both
the arrival and departure dates.

Approach:
Convert each date into its corresponding day of the year.

Create a helper function dayOfYear():
- Split the date into month and day.
- Store the number of days in each month.
- Calculate the total days in all previous months.
- Add the current day to get the day of the year.

Calculate the start and end days for both Alice and Bob.

The overlapping interval is:
- Start: Maximum of their arrival dates.
- End: Minimum of their departure dates.

Calculate the overlap using:
min(alice_end, bob_end) - max(alice_start, bob_start) + 1

If the result is positive, return it. Otherwise, return 0.

Time Complexity:
O(1)

Space Complexity:
O(1)
"""


class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:
        def dayOfYear(date: str) -> int:
            month, day = map(int, date.split("-"))

            days = [31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]

            total = sum(days[:month - 1])
            total += day

            return total

        alice_start = dayOfYear(arriveAlice)
        alice_end = dayOfYear(leaveAlice)

        bob_start = dayOfYear(arriveBob)
        bob_end = dayOfYear(leaveBob)

        days_together = (
            min(alice_end, bob_end)
            - max(alice_start, bob_start)
            + 1
        )

        return max(0, days_together)


if __name__ == "__main__":
    solution = Solution()

    print(solution.countDaysTogether(
        "08-15", "08-18", "08-16", "08-19"
    ))  # 3

    print(solution.countDaysTogether(
        "10-01", "10-31", "11-01", "12-31"
    ))  # 0

    print(solution.countDaysTogether(
        "01-01", "01-10", "01-10", "01-20"
    ))  # 1
