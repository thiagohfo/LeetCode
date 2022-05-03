class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_int = int(a, 2) + int(b, 2)
        return str(bin(sum_int))[2:]