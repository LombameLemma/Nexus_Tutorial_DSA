class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            greater = [element for element in nums if element < nums[i]]
            output.append(len(greater))
        return output
