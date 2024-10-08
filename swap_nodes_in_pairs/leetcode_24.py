from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nxt_pair = curr.next.next
            second = curr.next

            # reverse
            second.next = curr
            curr.next = nxt_pair
            prev.next = second

            # update
            prev = curr
            curr = nxt_pair

        return dummy.next