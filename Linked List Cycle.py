class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        copy=ListNode(0,head)
        fast=copy
        slow=copy
        if not fast.next:
            return False
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False

        
