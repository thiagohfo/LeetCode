class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_dict = {}

        for i in nums:
            if i in nums_dict.keys():
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1

        for i in nums_dict.values():
            if i % 2 == 0:
                continue
            else:
                return False

        return True