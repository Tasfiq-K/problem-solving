## The Problem

**[Last Moment Before All Ants Fall Out of a Plank](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/?source=submission-noac)**

This problem is quite easy to solve. Although it's of a medium difficulty, no idea why. However, understanding the problem is relatively easy. It says that, you will given two lists named `left` and `right` and the length of a plank `n`. The `left` and `right` might contain integers describes the ant(s) and their positions on the plank, also one of them could be empty but not both of them. 

Now for each unit of the time every ant on the plank moves **one unit** either to the left or to the right based on their positions by the two lists. The `left` list provides positions of the ants that move to their left, and the `right` list provides the positions of the ants that move to their right. As the time passes, ants move and to their left and right and eventually fall off the plank. Now, you need to find out the time it took for the last ant to fall of the plank. 

Now, when two collides while one moving to the left and another to its right, they start to go to the opposite direction, but no extra time passes. So, it's just means they cross each other. 

## The Approach
The problem might seem like a bit overwhelming, at least for the bit where the ants collide. But it really isn't. Let's go over the situation when they collide.

So, when the two collides, they change their directions, without spending any time. But this really doesn't change anything. Ok, so what do I mean by that.

Think of a number a line, expanding from 0 to 10, and there are two ants `A` and `B`. `A` is at position 3 going to the right of the number line, and `B` at position 5 going to the left of the number line. So, for `A` it should've taken 7 time steps to fall of the plank and for `B` it would've taken 5. But they collide at position 4 on the number line. But it doesn't really change anything. Because, **after** the collision ant `B` would be at position 5 again and ant `A` would be at 3. So, now, for `A` it will take 1 step to go position 4 + 1 step come back at position 3 + 3 steps to go to position 0, total 5 steps. And same calculation can be done for ant `B`, which will result in 7. So, the final result is the same as before.

But this could be though in another way. If we just simply say that the ants didn't collide and changed directions, but they just crossed each other, then it will be easier to grasp the concept. So, when the ants cross each other at a given position, it just takes the usual steps to reach the end of the plank.

The, solution approach is pretty simple:

1. First you check if the given `left` or `right` lists are empty or not.
2. If the `left` list is empty
    * return the `n` (plank length) - minimum value of the `right` list. 
3. If the `right` list is empty
    * return the maximum of the `left` list
4. If they are not empty
    * get the maximum value from the `left` list and `n` - minimum value from the `right` list and return the maximum from them


## The Code

```python
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left: 
            # return the plank length - min(right) if left list is empty. Because we subtract the total length of the plank from the ant who is at farthest to the left. Remember these ants are moving to the right side of the plank
            
            return n - min(right, default=0) 
            
        elif not right: 
            # return the maximum of the left list, which is at the farthest to the right. Remember these ants are moving to the left side of the plank
            return max(left) 
        
        # if the both list contains values
        left_val = max(left) # get the maximum from the left list
        right_val = n - min(right) # get the farthest left ant's time steps value
        
        return max(left_val, right_val) # return the maximum time steps
```