class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left:
            return n - min(right, default=0)
        elif not right:
            return max(left)
        
        left_val = max(left)
        right_val = n - min(right)
        
        return max(left_val, right_val)