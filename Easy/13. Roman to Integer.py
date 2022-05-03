class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_num = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                sum_num += (roman[s[i]] * -1)
            else:
                sum_num += roman[s[i]]

        sum_num += roman[s[-1]]

        return sum_num