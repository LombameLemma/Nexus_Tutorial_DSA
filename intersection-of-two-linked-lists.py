class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = [], []
        tempA, tempB = headA, headB
        while tempA:
            a.append(tempA)
            tempA = tempA.next
        while tempB:
            b.append(tempB)
            tempB = tempB.next
        if a[-1] != b[-1]:
            return None
        i, j = len(a) - 2, len(b) - 2
        while i >= 0 and j >= 0:
            if a[i] != b[j]:
                return a[i].next
            i -= 1
            j -= 1
        if i < 0:
            return a[0]
        if j < 0:
            return b[0]
