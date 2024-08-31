from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        matrix[0][0] = head.val
        head = head.next

        row, col, d_row, d_col, ROW, COL = 0, 0, 0, 1, range(m), range(n)

        while head:
            if (
                row + d_row in ROW
                and col + d_col in COL
                and matrix[row + d_row][col + d_col] == -1
            ):
                row += d_row
                col += d_col
                matrix[row][col] = head.val
                head = head.next
            else:
                # change the direction by 90 degree right
                # for a position (r, c) in a 2D vector
                # 90 degree change would be (c, -r)
                d_row, d_col = d_col, -d_row

        return matrix
