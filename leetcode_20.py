class Solution:
    def isValid(self, s: str) -> bool:
        open_paren = "({["
        balance = "(){}[]"

        stack = []

        if len(s) <= 1:
            return False
        
        for ch in s:
            if ch in open_paren:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                last_open = stack.pop()

                if last_open + ch not in balance:
                    return False
        
        return len(stack) == 0
