class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)):
            minimum_index = i
            
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum_index]: 
                    minimum_index = j
            
            arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
            
        return arr
