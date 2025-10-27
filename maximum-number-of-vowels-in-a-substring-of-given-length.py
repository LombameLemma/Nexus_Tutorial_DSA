class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        max_vowels = 0
        
        def is_vowel(char):
            return char in vowels

        for i in range(n - k + 1):
            
            current_vowels = 0
            
            for j in range(i, i + k):
                if is_vowel(s[j]):
                    current_vowels += 1
            
            max_vowels = max(max_vowels, current_vowels)
            
            if max_vowels == k:
                return k

        return max_vowels
