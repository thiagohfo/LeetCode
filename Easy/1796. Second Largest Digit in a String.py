class Solution:
    def secondHighest(self, s: str) -> int:
        nums = [str(i) for i in range(0, 10)]
        nums_list = []
        result = -1

        if len(s) > 0:
            for i in s:
                if i in nums and i not in nums_list:
                    nums_list.append(int(i))

            nums_list.sort(reverse=True)

            for i in range(0, len(nums_list) - 1):
                if nums_list[i] > nums_list[i + 1]:
                    return nums_list[i + 1]

        return result