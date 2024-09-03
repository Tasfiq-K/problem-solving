from typing import List

## My approach ##


# class Solution:
#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         n_elem = m * n
#         length = len(original)

#         if length != n_elem:
#             return []

#         mat_2d = [[-1] * n for _ in range(m)]

#         d_row, d_col, idx = 0, 0, 0

#         while idx < length:
#             if d_row in range(m) and d_col in range(n):
#                 mat_2d[d_row][d_col] = original[idx]
#                 d_col += 1
#                 idx += 1
#             else:
#                 d_col = 0
#                 d_row += 1

#         return mat_2d


## 2nd approach ##

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []

        if len(original) == m * n:
            for i in range(0, len(original), n):
                ans.append(original[i : i + n])
        return ans
