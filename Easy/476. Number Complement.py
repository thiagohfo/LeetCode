class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = str(bin(num)[2:])
        bin_complement = ''

        for i in bin_str:
            if i == '0':
                bin_complement += '1'
            else:
                bin_complement += '0'

        return int(bin_complement, 2)