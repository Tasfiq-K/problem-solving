from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Approach 1 ##
# class Solution:
#     def mergeInBetween(
#         self, list1: ListNode, a: int, b: int, list2: ListNode
#     ) -> ListNode:
#         merger = []

#         index = 0
#         cur1 = list1
#         while index < a:
#             merger.append(cur1.val)
#             cur1 = cur1.next
#             index += 1

#         cur2 = list2
#         while cur2:
#             merger.append(cur2.val)
#             cur2 = cur2.next

#         while index < b + 1:
#             cur1 = cur1.next
#             index += 1

#         while cur1:
#             merger.append(cur1.val)
#             cur1 = cur1.next

#         result = None
#         for i in range(len(merger)):
#             new_node = ListNode(merger.pop(), result)
#             result = new_node

#         return result


## Approach 2 ##

class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        
        top = list1
        changed_tail = None
        counter = 0

        while list1:
            counter += 1
            
            if counter == a:
                temp = list1.next # [9, 5]
                list1.next = list2 # [1000, 1001, 1002]
                changed_tail = list1.next
                list1 = temp # [9, 5]
            
            if counter == b:
                while changed_tail.next is not None:
                    changed_tail = changed_tail.next # [1002]

                changed_tail.next = list1.next # [1002, next: [None]]
                break
            
            list1 = list1.next

            if changed_tail and changed_tail.next is not None:
                changed_tail = changed_tail.next
        return top