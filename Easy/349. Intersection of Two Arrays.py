class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        final_list = []

        for i in nums2:
            if i in nums1 and i not in final_list:
                final_list.append(i)

        return final_list