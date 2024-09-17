from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_list = (s1 + " " + s2).split(" ")

        count_table = {}
        for word in word_list:
            if word in count_table:
                count_table[word] += 1
            else:
                count_table[word] = 1

        return [word for word in count_table if count_table[word] == 1]
