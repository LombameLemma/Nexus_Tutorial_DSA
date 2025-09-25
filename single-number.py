class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        res=Counter(nums)
        for i in res:
            if res[i]==1:
                return i
