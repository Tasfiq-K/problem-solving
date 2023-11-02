## The Problem
**[Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2023-11-02)**

The problem says that, given a root of a Binary Tree, you need to find out those nodes, which has the same value as the average of all it's child nodes and itself, and return the total count of them. This would be more clear with an example, suppose you have tree which is something like this:

                        4
                       / \
                      8   5
                     / \   \
                    0   1   6


so, in this tree, The root node is 4, and it has 2 leaf nodes (children), whcih has total 3 leaf nodes, now if you calculate the average considering the root node, then (4 + 8 + 5 + 0 + 1 + 6) / 6 = 4, so this is True, because the average value is equal to the root of the node. Now we calculate for every nodes, then count them. And the total count will be our desired answer.

## The Approach
The approach that I've taken is similar to the what's in the [editorial](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/editorial/?envType=daily-question&envId=2023-11-02) section for this problem. Which is traveersing the tree bottom up, and calculating the averages and counting them along the way. Let's break it down how this works. 

1. First we take a variable for counting, say, counter
2. Then we start at the first node (root) of the tree, and search for it's children (left node, right node) and follow them and look for their children, until we hit None.
3. When we reach the bottom (where there are null values or no other children found) we traverse back and calculate the averages for each existing node value, and store them if average value and the value of the current node is the same. While doing this, we also calculate how many existing node there is and also sum up the node's values.
4. This continues untill we reach the top, So, when are at the top, we already the total sum of all the other node values, and total number of existing nodes. Now we calculate for the average for the root node and compare the average with its value.

So, the calculation will look like this.

1. Let's start from the bottom of the left side, where last two children of the value 8 are 0 and 1. So, let's enter 0
2. For 0, there are no children nodes, so we calculate the average for 0 is 0 / 1 = 0 ( we devide by 1 is because 0 itself is an element). So average 0 is equal to the node value, so our counter goes up 1 value. Also we keep track of number of elements, so node count is now 1
3. Same goes for children node 1, the average is 1 + 0 / 1 = 1, the counter goes up again, and node count is now 2
4. Now for the node value 8, Counting this as a node, our node count is 3, and average is 8 + 0 + 1 / 3 = 3, not equal to the node value. So, our node count is 3 and counter is 2

[ This is the end of left side, and we store these values. Let's say total_left_node = 3, and total_average_count = 2 ]

[ Now for the right side, same approach]

5. For value 6, 6 / 1 = 6, So, we counter value and node count value goes up, so the counter value is 3 and node count value is 1
6. For value 5, as it has 6 as children node, the average is 5 + 6 / 2 = 5.5, we do floor division and count this as True. So, the counter value goes up again so is node count, they are 4 and 2 respectively.

[ This is the end of right side of the root node, let's store the values again, say, total_right_node = 2, total_average_count = 2 ]

7. Now for the root node, Let's first sum up the nodes, total_nodes = total_left_node + total_right_node + current_node = 3 + 2 + 1 = 6. Now the average is 4 + 8 + 5 + 0 + 1 + 6 / 6 = 4, which is equal to the node value, the counter goes up which is 5. We then, return this value as our result.

## The Code

```python
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def count_sum(node):
            nonlocal counter # using the counter variable as a nonlocal one, this means, the counter value outside this function will have same value after each update.
            if node == None: # if node None (when we hit bottom) return (0, 0)
                return (0, 0)

            left_sum, left_count = count_sum(node.left) # recurring on the left side, this will execute until we reach the bottom of the left side
            right_sum, right_count = count_sum(node.right) # recurring on the left side, this will execute until we reach the bottom of the right side

            node_sum = node.val + left_sum + right_sum # calculating the sum for each node 
            node_count = left_count + right_count + 1 # counting the nodes

            if (node_sum // node_count) == node.val: # chekcing if the averages matches the current node value, if it does counter goes up 1 value
                counter += 1

            return (node_sum, node_count)

        counter = 0 # initiating the counter variable
        count_sum(root) # calling the inner count_sum function

        return counter
```