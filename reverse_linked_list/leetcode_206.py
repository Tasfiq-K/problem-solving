from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # we will be updating this prev variable
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        return prev