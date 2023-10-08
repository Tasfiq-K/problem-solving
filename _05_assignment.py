class Solution:
    """
    A solution class
    """
    def addList(self, nums: list) -> list:
        """
        Adds the previous current indexed value to the previous index value
        and saves it inplace.
        Args:
            nums: [list]: A list of numbers
        
        Return: returns the modified list
        """

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums

res = Solution()
print(res.addList([1, 2, 3, 4, 5, 6, 7, 8]))