class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict

        counter = defaultdict(int)
        stack = [root] # we will create a list of the node objects. This will contain only the root node, which might or might not have children nodes

        # iterate over the stack (list) and pop until it's empty

        while stack:
            node = stack.pop()
            counter[node.val] += 1

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
            
            max_freq = max(counter.values())
            result = []

            for key in counter:
                if counter[key] == max_freq:
                    result.append(key)
            
        return result