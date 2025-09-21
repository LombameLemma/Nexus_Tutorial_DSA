class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix=[]
        first=strs[0]
        for i in range(len(first)):
            char=first[i]
            for str in strs[1:]:
              if i>=len(str) or str[i]!=char:
                return "".join(prefix)
            prefix.append(char)
        return "".join(prefix)
        
