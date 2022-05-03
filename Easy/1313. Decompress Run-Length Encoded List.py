class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        descom_list = []

        for i in range(0, len(nums), 2):
            descom_list.extend([nums[i + 1]] * nums[i])

        return descom_list