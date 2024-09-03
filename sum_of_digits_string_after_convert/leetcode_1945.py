class Solution:
    def getLucky(self, s: str, k: int) -> int:
        conv = "".join(str((ord(ss) - ord("a") + 1)) for ss in s)

        for _ in range(k):
            temp = 0
            for ss in conv:
                temp += int(ss)
                conv = str(temp)

        return temp
