class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def count_sum(node):
            nonlocal counter
            if node == None:
                return (0, 0)

            left_sum, left_count = count_sum(node.left)
            right_sum, right_count = count_sum(node.right)

            node_sum = node.val + left_sum + right_sum
            node_count = left_count + right_count + 1

            if (node_sum // node_count) == node.val:
                counter += 1

            return (node_sum, node_count)

        counter = 0
        count_sum(root)

        return counter