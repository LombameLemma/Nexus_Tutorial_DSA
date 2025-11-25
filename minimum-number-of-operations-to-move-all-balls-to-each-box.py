class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        count = 0
        left_ops = 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                count += 1
            left_ops += count
            answer[i] = left_ops
            
        count = 0
        right_ops = 0
        for i in range(n - 2, -1, -1):
            if boxes[i+1] == '1':
                count += 1
            right_ops += count
            answer[i] += right_ops
            
        return answer
