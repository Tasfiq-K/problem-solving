from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach 1

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited_nodes = set()
#         current_node = head

#         while current_node:
#             if current_node in visited_nodes:
#                 return True
#             visited_nodes.add(current_node)
#             current_node = current_node.next

#         return False

# Approach 2


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True

        return False
