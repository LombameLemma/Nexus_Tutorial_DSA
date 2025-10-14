class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        max_coins = 0
        for i in range(n):
            max_coins += piles[-2 - 2*i]
        return max_coins
