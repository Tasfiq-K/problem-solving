class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        high = target[-1]
        val_range = [val for val in range(1, high + 1)]
        
        out = []
        
        for val in val_range:
            if val not in target:
                out.append("Push")
                out.append("Pop")
            else:
                out.append("Push")
            
        return out