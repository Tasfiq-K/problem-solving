class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefix_xor = 0
        character_map = [0] * 26
        character_map[ord("a") - ord("a")] = 1 # place 1 at position 0
        character_map[ord("e") - ord("a")] = 2 # place 2 at position 4
        character_map[ord("i") - ord("a")] = 4 # place 4 at position 8 and so on..
        character_map[ord("o") - ord("a")] = 8
        character_map[ord("u") - ord("a")] = 16

        mp = [-1] * 32
        longest_substring = 0

        for i in range(len(s)):
            prefix_xor ^= character_map[ord(s[i]) - ord("a")]
            # print(prefix_xor)
            if mp[prefix_xor] == -1 and prefix_xor != 0:
                mp[prefix_xor] = i
            longest_substring = max(longest_substring, i - mp[prefix_xor])
        
        return longest_substring