from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Approach 1: using stack

# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = []
#         cur = head

#         while head:
#             stack.append(cur)
#             cur = cur.next
        
#         cur = stack.pop()
#         maxVal = cur.val
#         result_list = ListNode(maxVal)

#         while stack:
#             cur = stack.pop()

#             if cur.val < maxVal:
#                 continue

#             else:
#                 new_node = ListNode(cur.val, result_list)
#                 result_list = new_node
#                 maxVal = cur.val
        
#         return result_list
    
## approach 2: Recursion ##

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        next_node = self.removeNodes(head.next)

        if head.val < next_node.val:
            return next_node
        
        head.next = next_node
        return head