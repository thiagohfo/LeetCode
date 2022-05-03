class Solution:
    def isHappy(self, n: int) -> bool:
        def number_next(n):
            sum_number = 0

            while n > 0:
                n, digit = divmod(n, 10)
                sum_number += digit ** 2

            return sum_number

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = number_next(n)

        return n == 1