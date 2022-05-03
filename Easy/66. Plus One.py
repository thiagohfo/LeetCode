class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ''.join(map(str, digits))
        number = int(number_str)
        number += 1
        number_str = str(number)
        new_list = [int(x) for x in number_str]

        return new_list