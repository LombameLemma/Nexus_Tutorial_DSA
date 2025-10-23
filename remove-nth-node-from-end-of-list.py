# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        copy=ListNode(0,head)
        slow=copy
        fast=copy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return copy.next
        
        
        """copy = ListNode(0, head)
        slow = copy
        fast = copy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return copy.next"""
