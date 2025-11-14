class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(temperatures)
        s=[]
        for j,val in enumerate(temperatures):
            while s and val>temperatures[s[-1]]:
                p=s.pop()
                ans[p]=j-p
            s.append(j)
        return ans
