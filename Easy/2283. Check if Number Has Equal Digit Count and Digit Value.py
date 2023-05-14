class Solution:
    def digitCount(self, num: str) -> bool:
        nums_dict = {}

        for i in range(10):
            nums_dict[i] = 0

        for i in num:
            if int(i) in nums_dict.keys():
                nums_dict[int(i)] += 1

        for i in range(len(num)):
            if int(num[i]) == nums_dict[i]:
                continue
            else:
                return False

        return True