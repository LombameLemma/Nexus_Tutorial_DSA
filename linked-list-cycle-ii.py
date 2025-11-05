class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                pointer1 = head
                pointer2 = slow 
                
                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                
                return pointer1 
                
        return None
