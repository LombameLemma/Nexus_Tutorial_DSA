class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        left,right=0 ,len(height)-1
        while left < right:
            width=right-left
            length= min(height[right],height[left])
            area = width *  length
            max_area= max(area,max_area)
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return max_area 
