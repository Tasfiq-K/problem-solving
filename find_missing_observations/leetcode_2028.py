from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_elem = len(rolls) + n
        remaining = (total_elem * mean) - sum(rolls)

        if remaining > 6 * n or remaining < n:
            return []

        q, r = divmod(remaining, n)  # returns, quotient and remainder

        return [q] * (n - r) + [q + 1] * r
