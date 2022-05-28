class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0

        sum_total = 0

        digits = ''

        while n:
            digits += str(int(n % k))
            n //= k

        for i in digits:
            sum_total += int(i)

        return sum_total
