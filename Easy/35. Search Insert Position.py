class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
            elif (i + 1) == len(nums) and nums[i] < target:
                return i + 1