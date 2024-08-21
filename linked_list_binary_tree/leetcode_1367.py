from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isEqual(TreeNode, ListNode):
            if not ListNode:  # we have exhausted all the nodes, so return
                return True
            if (
                not TreeNode or TreeNode.val != ListNode.val
            ):  # compare the node's values and the see if Treenode is empty or not
                return False
            return isEqual(TreeNode.left, ListNode.next) or isEqual(
                TreeNode.right, ListNode.next
            )  # Recursive call

        q = deque([root])

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.val == head.val and isEqual(cur, head):
                    return True
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return False
