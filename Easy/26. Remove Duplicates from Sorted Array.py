class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []
        count = 0

        for i, num in enumerate(nums):
            if num in new_nums:
                nums[i] = 101
            else:
                new_nums.append(num)
                count += 1

        nums.sort()

        return count
