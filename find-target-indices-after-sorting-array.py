class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()        
        x = []
        for i in range(len(nums)):
            if nums[i] == target:
                x.append(i)                
        return x
