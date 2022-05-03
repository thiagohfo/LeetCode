class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
        else:
            if len(nums2) > 0:
                for i in range(len(nums1)):
                    if nums1[i] == 0:
                        for j in range(len(nums2)):
                            if nums2[j] != '_':
                                nums1[i] = nums2[j]
                                nums2[j] = '_'
                                break

            nums1.sort()