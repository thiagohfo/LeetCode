class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_dict = {}
        max_num = 0

        for i in nums:
            if i in nums_dict.keys():
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        for i in nums_dict.keys():
            if i + 1 in nums_dict.keys():
                if (nums_dict[i] + nums_dict[i + 1]) > max_num:
                    max_num = nums_dict[i] + nums_dict[i + 1]

            if i - 1 in nums_dict.keys():
                if (nums_dict[i] + nums_dict[i - 1]) > max_num:
                    max_num = nums_dict[i] + nums_dict[i - 1]

        return max_num