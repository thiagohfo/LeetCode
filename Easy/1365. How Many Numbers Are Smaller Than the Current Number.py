class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallers = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    smallers[i] += 1

        return smallers