from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        output = []
        length = len(nums)
        start, end = 0, 0

        while start < length and end < length: # loop over to the end of the list
            if (end + 1) < length and nums[end + 1] == nums[end] + 1:
                end += 1
            else:
                if nums[start] == nums[end]:
                    output.append(str(nums[start]))
                    start += 1
                    end += 1
                else:
                    output.append( str( nums[ start ] ) + "->" + str( nums[ end ] ) )
                    end += 1
                    start = end
        
        return output