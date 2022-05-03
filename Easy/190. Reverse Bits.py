class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = str(bin(n + 2 ** 32))[:2:-1]

        return int(bin_str, 2)
