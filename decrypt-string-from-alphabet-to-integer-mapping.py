class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1
        
        while i >= 0:
            if s[i] == '#':
                num_str = s[i-2:i]
                num = int(num_str)
                result.append(chr(ord('j') + num - 10))
                i -= 3
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i -= 1
        
        return "".join(reversed(result))
