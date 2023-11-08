## The Problem
**[Determine if a Cell Is Reachable at a Given Time](https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/?envType=daily-question&envId=2023-11-08)**

The problem is quite straigtforward. In a given 2D grid system, you have to determine if you can reach `block B` from `Block A` at a certain given time `t`. You will be provided with the block coordinates and the time `t`

## The Approach
The approach is also pretty straigtforward, but there are few edge cases, which makes te problem bit interesting.

So, as the problem is related to calculation of distance, you might be tempted to use the Eucleadian distance formula, but that's actually won't work here. Because, the Eucleadian distance is for two points in a space. But here, it's not distance between points, rather distance between grid blocks. This calls for the `Chevyshev distance` also known as `chessboard` distance. Look them up, if you don't know how to calculate this distance between to grid blocks. 

The `Chevyshev distance` is also quite straightforward, The equation is $$ max(|x_2 - x_1|, |y_2 -y_1|)$$

Given, the Cartesian coordinates of the two blocks.

So, to tackle this problem, we just calculate this distance from the two blocks and see if it's within the given time `t`. Which means, if the distance is equal or less than the time `t`. But there is an edge cases. This won't work when the two blocks are on the same place and the given time `t` is only 1 unit of time. Think about the time `t` is as steps. So, when the `Block A` and `Block B` are at the same place, you can't take 1 step and reach `Block B` from `A`. Because you are already on it. So we just handle this one edge case.

## The Code
```python
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if t == 1 and sx == fx and sy == fy: # when the two blocks have the same coordinates (they are at the same place) and the step (time) needed is one, return False
            return False

        return max( abs(fx - sx), abs(fy - sy) ) <= t # otherwise, just return if the Chevyshev distance is equal or less than the given step (time)
```