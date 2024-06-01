class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} # to keep track of the indices of tha characters
        left, right = 0, 0 # start two pointer from position 0
        longest = 1 # longest streak counter

        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            longest = max(longest, right - left + 1)
            seen[s[right]] = right # map the character with its current index
            right += 1 # move right pointer to the next index

        return longest
