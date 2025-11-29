
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        
        remaining_piles = piles[n // 3:]
        
        max_coins = sum(remaining_piles[::2])
        
        return max_coins
