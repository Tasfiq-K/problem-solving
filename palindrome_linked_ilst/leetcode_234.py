from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# solution 1

# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         list_vals = []

#         while head:
#             list_vals.append(head.val)
#             head = head.next
        
#         l, r = 0, len(list_vals) - 1

#         while l < r and list_vals[l] == list_vals[r]:
#             l += 1
#             r -= 1
#         return l >= r 
    
# solution 2

class Solution:

    def reverse(sefl,  head: Optional[ListNode]) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = self.reverse(slow)

        while rev:
            if head.val != rev.val:
                return False
            rev = rev.next
            head = head.next
        
        return True
        

    


