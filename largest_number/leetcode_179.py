from typing import List


# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         num_strings = [str(num) for num in nums]

#         num_strings.sort(key=lambda a: a * 10, reverse=True)

#         if num_strings[0] == "0":
#             return "0"
        
#         return "".join(num_strings)
    

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self._quick_sort(nums, 0, len(nums) - 1)
        largest_num = "".join(map(str, nums))

        return "0" if largest_num[0] == 0 else largest_num
    
    def _quick_sort(self, nums: List[int], left: int, right: int) -> None:
        if left >= right:
            return 
        
        pivot_index = self._partition(nums, left, right)

        self._quick_sort(nums, left, pivot_index - 1)
        self._quick_sort(nums, pivot_index + 1, right)

    def _partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        low_index = left

        for i in range(left, right):
            if self._compare(nums[i], pivot):
                nums[i], nums[low_index] = nums[low_index], nums[i]
                low_index += 1
        
        nums[low_index], nums[right] = nums[right], nums[low_index]
        return low_index
    
    def _compare(self, first_num: int, second_num: int) -> bool:
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)
    
sol = Solution()
largest_num = sol.largestNumber([3, 30, 34, 5, 9])
print(largest_num)
