class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_digitis = 0
        num_str = str(n)

        for i in num_str:
            product *= int(i)
            sum_digitis += int(i)

        return product - sum_digitis