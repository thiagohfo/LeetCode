class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num = nums[0]

        for i in range(1, len(nums)):
            num *= nums[i]

        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0