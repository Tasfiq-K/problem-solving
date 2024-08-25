from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        ht = defaultdict(int)

        while headA:
            ht[headA] = 1
            headA = headA.next
        
        while headB:
            if ht[headB]:
                return headB
            headB = headB.next
        
        return None