class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        total_sum = sum(skill)
        
        if total_sum * 2 % n != 0:
            return -1
        
        target_skill = total_sum * 2 // n
        
        skill.sort()
        
        left = 0
        right = n - 1
        total_chemistry = 0
        
        while left < right:
            team_skill_sum = skill[left] + skill[right]
            
            if team_skill_sum != target_skill:
                return -1
            
            chemistry = skill[left] * skill[right]
            total_chemistry += chemistry
            
            left += 1
            right -= 1
            
        return total_chemistry

        
