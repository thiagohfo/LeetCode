class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        count = 1
        i = 1
        grow = False

        if n > 0:
            nums = [0, 1]
        elif n == 0:
            return 0

        while count < n:
            if grow == False:
                nums.append(nums[i])
                grow = True
            else:
                nums.append(nums[i] + nums[i + 1])
                grow = False
                i += 1
            count += 1

        return max(nums)
