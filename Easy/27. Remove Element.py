class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                count += 1

                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] != '_' and nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = '_'
                        break

        return len(nums) - count