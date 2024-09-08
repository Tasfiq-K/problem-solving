from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k

        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        split_size = size // k
        remaining_part_size = size % k

        cur = head
        prev = cur

        for i in range(k):
            new_part = cur
            cur_size = split_size

            if remaining_part_size > 0:
                remaining_part_size -= 1
                cur_size += 1
            
            j = 0
            while j < cur_size:
                prev = cur
                if cur:
                    cur = cur.next
                j += 1
            
            # unlinking the rest of the node
            # basically for a list [1, 2, 3, 4, 5]
            # if cur is at 3 then prev will be at 2
            # so we are unliking the list by putting prev.next = None
            if prev:
                prev.next = None

            ans[i] = new_part
        
        return ans