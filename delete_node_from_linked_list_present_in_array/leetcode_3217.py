from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        nums = set(nums)
        while head:
            if head.val in nums:
                head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = head
        
        return dummy.next
        