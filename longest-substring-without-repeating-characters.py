class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = set()
        maxx = 0
        i = 0
        for j in range(n):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            maxx = max(maxx, len(window))
        return maxx
