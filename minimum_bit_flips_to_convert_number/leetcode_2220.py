# from typing import List


# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:
#         count = 0

#         while start > 0 or goal > 0:
#             if (start & 1) != (goal & 1):
#                 count += 1
#             start >>= 1
#             goal >>= 1
#         return count


## Approach 2: recursion

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == 0 and goal == 0:
            return 0
        
        flip = 1 if (start & 1) != (goal & 1) else 0

        return flip + self.minBitFlips(start >> 1, goal >> 1)