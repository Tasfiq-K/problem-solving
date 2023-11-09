class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        curr_streak = 0
        MOD = 10 ** 9 + 7

        length = len(s)

        for indx in range(length):
            if indx == 0 or s[indx] == s[indx - 1]:
                curr_streak += 1
            else:
                curr_streak = 1
        
            ans = (ans + curr_streak) % MOD
        
        return ans
