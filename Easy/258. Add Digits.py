class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            while num > 9:
                sum_total = 0
                str_num = str(num)

                for i in str_num:
                    sum_total += int(i)

                num = sum_total

            return sum_total