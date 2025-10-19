class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counts=0
        l,r=0,len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            if sum==k:
                counts+=1
                r-=1
                l+=1
            elif sum < k:
                l+=1
            else:
                r-=1
        return counts
        
        
        """counts=Counter(nums)
        operations=0
        for num in list(counts.keys()):
            complement=k-num
            if complement < num:
                continue
            elif complement==num:
                operations += counts[num] // 2
            else:
                if complement in counts:
                    pairs=min(counts[num],counts[complement])
                    operations += pairs
                    counts[complement]=0
        return operations"""
            
          
