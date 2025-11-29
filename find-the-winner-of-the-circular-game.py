class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        winner_pos_0_indexed = 0 
        
        for i in range(1, n + 1):
            winner_pos_0_indexed = (winner_pos_0_indexed + k) % i
            
        return winner_pos_0_indexed + 1
