#### Solution of leetcode problem valid parenthesis using two pointer approach ####

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0 
        close_count = 0
        length = len(s) - 1

        for pos in range(length + 1):
            if s[pos] == "(" or s[pos] == "*":
                open_count += 1
            else: 
                open_count -= 1

            if s[length - pos] == ")" or s[length - pos] == "*":
                close_count += 1
            else:
                close_count -= 1
            
            if open_count < 0 or close_count < 0:
                return False
        
        return True
