class Solution:
    def reverseVowels(self, s: str) -> str:
       vowels = set('aeiou')
       s = list (s)
       i,j= 0, len(s) -1
       while i<j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i].lower() in vowels and s[j].lower() not in vowels:
                j-=1
            elif s[i].lower() not in vowels and s[j].lower() in vowels:
                i+=1
            else:
                i+=1
                j-=1



    
       
       return ''.join(s)
       
