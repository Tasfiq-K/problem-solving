from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        all_clear = False

        for word in words:
            for w in word:
                if w not in allowed:
                    all_clear = False
                    break
                else:
                    all_clear = True
            
            if all_clear:
                count += 1
        
        return count