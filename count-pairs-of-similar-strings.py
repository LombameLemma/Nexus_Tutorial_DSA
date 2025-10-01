class Solution:
    def similarPairs(self, words: list[str]) -> int:
        from collections import defaultdict
        x = defaultdict(int)
        for word in words:
            normalized_word = "".join(sorted(list(set(word))))
            x[normalized_word] += 1
        s= 0
        for count in x.values():
            if count > 1:
                s += (count * (count - 1)) // 2

        return s




