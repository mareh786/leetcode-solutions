"""
LeetCode 2243 - Calculate Digit Sum of a String

Difficulty: Easy
Topic: String / Simulation

Problem Summary:
Given a string s containing digits and an integer k,
repeatedly divide the string into consecutive groups of k digits.

Calculate the sum of digits in each group and concatenate
the resulting sums.

Repeat until the string length is less than or equal to k.

Approach:
1. Continue while len(s) > k.
2. Initialize an empty string ans.
3. Divide s into groups of size k.
4. Calculate the sum of digits in each group.
5. Append each group's sum to ans.
6. Update s = ans and repeat.
7. Return the final string.

Time Complexity: O(n log_k(n)) approximately
Space Complexity: O(n)
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                grp = s[i:i + k]

                total = 0
                for digit in grp:
                    total += int(digit)

                ans += str(total)

            s = ans

        return s


if __name__ == "__main__":
    solution = Solution()

    print(solution.digitSum("11111222223", 3))  # 135
    print(solution.digitSum("00000000", 3))     # 000
    print(solution.digitSum("1234", 2))         # 37
