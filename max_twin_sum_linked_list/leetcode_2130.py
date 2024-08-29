from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## Approach 1 ##


# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         stack = []

#         while head:
#             stack.append(head.val)
#             head = head.next

#         left = 0
#         right = len(stack) - 1
#         summ = float(-inf)

#         while left < right:
#             if stack[left] + stack[right] > summ:
#                 summ = stack[left] + stack[right]
#             left += 1
#             right -= 1

#         return summ

## Approach 2 ##


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxVal = 0
        slow = fast = head

        # go to the middle of the list

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # slow will be at the middle of the list

        # Reverse the list from the middle, basically where slow pointer is pointing at

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            head = head.next
            prev = prev.next

        return maxVal
