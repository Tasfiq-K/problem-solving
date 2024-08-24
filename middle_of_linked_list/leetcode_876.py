from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
A great analogy of the solution is that, if you and your friend are climbing staris,
where you are climbing one step at a time and your frined two steps at a time.
By the time your friend reaches the end where you will be?

Well, the answer is at the middle
"""


class Solution:
    def MiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Take two pointers

        fast = slow = ListNode()

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
