
"""
LeetCode 507 - Perfect Number

Difficulty: Easy
Topic: Math / Number Theory

Problem Summary:
A perfect number is a positive integer that is equal to
the sum of its positive divisors, excluding itself.

Example:
28 = 1 + 2 + 4 + 7 + 14

Approach:
1. Handle num = 1 separately because it is not a perfect number.
2. Initialize total = 1 because 1 divides every positive integer greater than 1.
3. Iterate from 2 to sqrt(num).
4. If num is divisible by i:
   - Add i to total.
   - Add num // i (its corresponding divisor).
5. Return whether total equals num.

Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        total = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i + num // i

                # Avoid counting the square root twice
                if i == num // i:
                    total -= i

        return total == num


if __name__ == "__main__":
    solution = Solution()

    print(solution.checkPerfectNumber(28))  # True
    print(solution.checkPerfectNumber(6))   # True
    print(solution.checkPerfectNumber(12))  # False
    print(solution.checkPerfectNumber(1))   # False
