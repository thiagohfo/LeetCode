class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        loop = True
        cont = 1
        step_by_step = [0] * len(nums)

        while loop:
            cont2 = cont
            for i, value in enumerate(nums):
                cont2 += nums[i]
                step_by_step[i] = cont2

            if min(step_by_step) < 1:
                cont += 1
                step_by_step = [0] * len(nums)
            else:
                loop = False

        return cont
