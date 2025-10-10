class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        forsort=[]
        for i in range(len(names)):
           
            forsort.append([names[i], heights[i]])
        forsort.sort(key=lambda x: x[1], reverse=True)
        ans=[]
        for person in forsort:
            ans.append(person[0])
        return ans
       
