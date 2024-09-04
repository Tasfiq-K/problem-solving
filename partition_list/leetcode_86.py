from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # [1, 4, 3, 2, 5, 2] -> [1, 2, 2, 4, 3, 5]

        # সো, আমাদের দুইটা লিস্ট জোড়া লাগাইতে হবে,
        # একটার মধ্যে x এর আগে যেসব ভ্যালু হয় সেগুলা থাকবে
        # অন্যটায় x অথবা x এর চেয়ে বড় এমন সংখ্যা গুলো থাকবে
        # তবে অবশ্যই order of apeearance বজায় রাখতে হবে

        # সো, দুইটা লিস্ট নেয়া যাক

        before_x = ListNode()
        x_and_after = ListNode()
        cur_1 = before_x
        cur_2 = x_and_after

        while head:  # looping through the head node
            if head.val < x:
                cur_1.next = head
                cur_1 = cur_1.next
            else:
                cur_2.next = head
                cur_2 = cur_2.next
            head = head.next

        cur_2.next = None
        cur_1.next = x_and_after.next

        return before_x.next
