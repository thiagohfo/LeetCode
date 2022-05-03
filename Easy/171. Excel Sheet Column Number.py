class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum_col = 0

        for i in columnTitle:
            sum_col = sum_col * 26
            sum_col += ord(i) - 64

        return sum_col