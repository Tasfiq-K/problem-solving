# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         bin_list = []
#         while head:
#             bin_list.append(head.val)
#             head = head.next

#         summ = 0
#         for i, k  in enumerate(bin_list[::-1]):
#             summ += k * 2**i

#         return summ

#### Another approach ####
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0

        while head:
            ans = 2 * ans + head.val
            head = head.next

        return ans
