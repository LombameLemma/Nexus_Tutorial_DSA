

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            target_index = nums[i]
            final_value = nums[target_index]
            ans.append(final_value)
        return ans
