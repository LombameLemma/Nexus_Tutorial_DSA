class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = []        
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                merged.append(word1[i])
                i += 1
            else:
                merged.append(word2[j])
                j += 1
                   
        merged.extend(word1[i:])
        merged.extend(word2[j:])

        return ''.join(merged)
