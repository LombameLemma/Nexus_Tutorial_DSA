class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            current_char = s[right]
            freq_map[current_char] = freq_map.get(current_char, 0) + 1
            
            max_freq = max(max_freq, freq_map[current_char])
            
            window_length = right - left + 1
            replacements_needed = window_length - max_freq
            
            if replacements_needed > k:
                left_char = s[left]
                freq_map[left_char] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)

        return max_len
