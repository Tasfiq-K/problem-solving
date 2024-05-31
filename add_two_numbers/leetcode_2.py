# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, 
                      l1: Optional[ListNode], 
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            summ = l1_val + l2_val + carry
            carry = summ // 10
            new_node = ListNode(summ % 10)

            curr.next = new_node # linking the new_node as the next node of the curr
            curr = new_node # moving the head pointer of the current to the new node 

            l1 = l1.next if l1 else None # moving to the next element of the node else None for l1
            l2 = l2.next if l2 else None # moving to the next element of the node else None for l2
        
        return dummy_head.next # returning the next node of the dummy head which was constructed by the curr