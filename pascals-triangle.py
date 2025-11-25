class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle=[]
        for numrow in range(numRows):
            currentrow=[1]
            if numrow>0:
                prev=triangle[-1]                
                for j in range(1,numrow):
                    newvalue=prev[j-1]+prev[j]
                    currentrow.append(newvalue)
                currentrow.append(1)
            triangle.append(currentrow)
        return triangle

        
