## The Problem
**[Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03)**

At a first glance, this might seem like difficult problem, and it's branded as a *medium* one, I don't why. But it isn't a problem of medium difficulty. If you know how to create a list and logically append something to it, you're good to go. 

So, let's go over the problem, The problem says, you'll be given a list of numbers and an integer value. You'll need to output a list containing the two operations of a stack "push" and "pop". You will add the "push", "pop" considering the numbers in the given target list. Which means, if a number exists in the `target list` you add a "push" to your output list, and if a number doesn't then you add **"pop"** followed by a **"push"**. That's it. That is the problem. But the catch is here. When the item isn't present you add an extra **push** before you add **pop**. It seems easy now, doesn't it!! ok, let's see how to solve this.

## The Approach

The approach is pretty simple one. Let's go over it one by one--

1. So, you'll be given a target list in the format of [1, n]. 1 is the lower range, n is the upper. `n` will be provided. The target contains some integer number(s), which are strictly increasing up to `n` but could be less than `n`. So, the thing is you don't need to consider the `n` a bit. It's just there.
2. Then you create your own range of values from 1 to the last value of the target + 1
3. Create a list to store the **Push** and **Pop**
4. Then iterate ove the range of values you created
    * if the number in your range of values is in the target
        * add a **Push** to the output list
    * if the number in your range of range of values is **not** in the target
        * add a **Push**, then immediately add a **Pop** (It's just we don't want the numbers that are not present in the target list, so, first add it to the stack (list) and take it out)
5. Return your output list

## The Code
```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        high = target[-1] # the higher range, last element of the target list
        val_range = [val for val in range(1, high + 1)] # create your range of values, ranges from 1 to high + 1 
        
        out = [] # your output list, which will contain the "push" and "pop" strings
        
        for val in val_range: # iterate over the range of values you created
            if val not in target: # check if the value exists or not, if not then add push and then add pop to the out list
                out.append("Push")
                out.append("Pop")
            else: # if value exists in the target list, adding "push" will be enough
                out.append("Push")
            
        return out # well return your answer! 
```