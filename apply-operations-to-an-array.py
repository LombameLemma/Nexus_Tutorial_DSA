class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            else:
                pass
        for j in nums:
            if j != 0:
                new_list.append(j)
            else:
                pass
        for k in range(len(nums)-len(new_list)):
            new_list.append(0)
        return new_list
