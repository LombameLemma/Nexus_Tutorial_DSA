class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            minimum = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr [i]:
                    minimum = j
                arr [i],arr[minimum ] = arr[minimum], arr[i]
                
        return arr
