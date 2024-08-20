from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0  # counter

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

#### Another approach ####

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         j = 0
#         # length = len(nums)
        
#         while j < len(nums):
#             if nums[j] == val:
#                 nums.pop(j)
#             else:
#                 j += 1
    
#         return j