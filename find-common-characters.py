import collections
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        if not words:
            return []
        common_counts = collections.Counter(words[0])
        for i in range(1, len(words)):
            current_counts = collections.Counter(words[i])
            for char in common_counts:
                common_counts[char] = min(common_counts[char], current_counts[char])
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)
        return result 
