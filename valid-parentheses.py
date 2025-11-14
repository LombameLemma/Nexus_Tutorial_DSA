class Solution:
    def isValid(self, s: str) -> bool:
        pare={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in pare.values():
                stack.append(i)
            else:
                if not stack or stack[-1] != pare[i]:
                    return False
                stack.pop()
        return not stack
       









        
        
        
        
        
        
"""stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack"""
        





