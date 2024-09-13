from typing import List

# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         prefix_xor = [0] * len(arr) + 1

#         for idx in range(len(arr)):
#             prefix_xor[idx + 1] = prefix_xor[idx] ^ arr[idx]

#         result = [prefix_xor[right + 1] ^ prefix_xor[left] for left, right in queries]

#         return result


## 2nd approach


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []

        for idx in range(1, len(arr)):
            arr[idx] ^= arr[idx - 1]

        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])

        return result
