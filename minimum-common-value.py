class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1 = 0  
        p2 = 0  
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        while p1 < len1 and p2 < len2:
            
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else: 
                p2 += 1
        return -1
