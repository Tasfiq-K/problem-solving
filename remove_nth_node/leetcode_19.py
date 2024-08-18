from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # take two pointers, one is fast, other is slow
        fast = head
        slow = head
        
        # Advance fast pointer to the nth position, mainly advance it n position ahead of slow pointer
        for _ in range(n):
            fast = fast.next

        # if fast pointer at the n position is None, then just return the next of the head pointer
        if not fast: 
            return head.next
        
        # now moave the slow pointer, the slow pointer will be n position apart from the fast pointer
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # now, the slow pointer will be just before the node that we want to delete, so delete the next node
        # simply point the next of the next node to the next node of the slow pointer
        slow.next = slow.next.next
        # return the linked list
        return head