class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        r_num1 = str(num)[::-1]

        for i in r_num1:
            if i == '0':
                r_num1 = r_num1[1:]
            else:
                break

        r_num2 = int(r_num1[::-1])

        if num == r_num2:
            return True
        else:
            return False