class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        copy=ListNode(0,head)
        left=copy
        right=copy
        if not right.next:
            return False
        while right.next and right.next.next:
            right=right.next.next
            left=left.next
            if right==left:
                return True
        return False
            
