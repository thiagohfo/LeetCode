class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_temp = {}

        for i in nums:
            if i in dict_temp.keys():
                dict_temp[i] += 1
            else:
                dict_temp[i] = 1

        value = min(dict_temp, key=dict_temp.get)

        return value