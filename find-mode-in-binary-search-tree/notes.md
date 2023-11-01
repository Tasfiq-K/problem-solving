## The Problem
In simple terms, the problem is that, you will provided a Binary Search Tree, where you will need to find the mode(s). A mode is a value that has the maximum frequency. There could be multiple modes, which means multiple items can be occured maximum frequency of time.

## The Approach
There are a lot of approaches for solving this problem. You can checkout the [Editorial](https://leetcode.com/problems/find-mode-in-binary-search-tree/editorial/?envType=daily-question&envId=2023-11-01) section for this problem, which is a very usefule resource. Also you might want to learn terms like `BFS`, `DFS`, `Stack`, `Queue`, `LIFO`, `FIFO` etc. Also don't forget to checkout what's a Binary Tree is.

The approach I have taken is a simple one:
1. Creating a stack using a list with the tree elements
2. Removing elements after counting and storing each occurance of an item in a dictionary
3. When the stack is exhausted, get the maximum occurance number or `max_freq` from the dictionary values
4. Then check the keys of the dictionary to get the keys that has occurance number equal to the `max_freq`

## The Code

```python
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict

        counter = defaultdict(int) # creating the dictionary
        stack = [root] # creating the list with the tree element(s)

        while stack: # iterate until stack is exhausted
            node = stack.pop() # take out the tree element
            counter[node.val] += 1 # count 

            if node.left: # check for the left item of the current node value
                stack.append(node.left)

            if node.right: # check for the right item of the current node value
                stack.appedn(node.right)
            
            max_freq = max(counter.values()) # get the maximum number 
            result = []

            for key in counter: # search for key(s) that occured max_freq time
                if counter[key] == max_freq:
                    result.append(key) # append key(s)
            
        return result
```