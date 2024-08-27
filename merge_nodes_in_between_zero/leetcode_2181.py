from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next  # Pointing to the second node of the head list
        next_sum = modify   # pointing to whatever modify is pointing to

        while next_sum:
            summ = 0
            if next_sum.val != 0:
                summ += next_sum.val
                next_sum = next_sum.next
            
            # at this moment next_sum is at a node which has value 0
            modify.val = summ # update the current value of the that the modify is pointing to
            next_sum = next_sum.next # so we move next_sum to a non zero node
            # we add next_sum pointer node to the next node of the modify where next_sum is currently at
            modify.next = next_sum 
            # we then also move the modify pointer to point at the non zero node
            # basically the modify and next_sum is pointing to the same node now
            modify = modify.next
        
        return head.next