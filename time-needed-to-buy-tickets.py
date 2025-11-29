from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        total_time = 0
        
        tickets_k = tickets[k]
        
        for i in range(len(tickets)):
            
            if i <= k:
                total_time += min(tickets[i], tickets_k)
            else:
                total_time += min(tickets[i], tickets_k - 1)
                
        return total_time
