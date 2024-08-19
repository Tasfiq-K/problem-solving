from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        j = 0
        length = len(nums)

        for i in range(1, length):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        print(j + 1)

sol = Solution()

sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])