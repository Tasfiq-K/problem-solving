# 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        pair = 0

        for ch in s:
            if ch == 'R':
                r_count += 1
            elif ch == 'L':
                l_count += 1
            if r_count == l_count:
                pair += 1
        return pair

