class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            current_value = nums[i] 
            j = i - 1 
            while j >= 0 and nums[j] > current_value: 
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = current_value 
            
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """for i in range(len(nums)):
            temp=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    change=j
                    nums[i],nums[j]=nums[j],nums[i]
                else:
                    nums[i],nums[j]=nums[i],nums[j]
            return nums"""
        
