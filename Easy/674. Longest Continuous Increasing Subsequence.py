class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        temp_longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp_longest += 1

                if temp_longest > longest:
                    longest = temp_longest
            else:
                if temp_longest > longest:
                    longest = temp_longest
                    temp_longest = 1
                else:
                    temp_longest = 1

        return longest
