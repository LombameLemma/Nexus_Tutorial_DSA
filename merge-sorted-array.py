class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while i < m + n and j < n:   
            if i < m and nums1[i] != 0 and nums1[i] >= nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                nums2.sort()  
                i += 1
            elif nums1[i] == 0:  
                nums1[i] = nums2[j]
                j += 1
                i += 1
            else:  
                i += 1

        print(nums1.sort())
