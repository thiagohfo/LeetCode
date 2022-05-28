class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict_nums = {}
        sum_nums = 0

        for i in nums:
            if i in dict_nums.keys():
                dict_nums[i] += 1
            else:
                dict_nums[i] = 1

        for key, value in dict_nums.items():
            if value == 1:
                sum_nums += key

        return sum_nums