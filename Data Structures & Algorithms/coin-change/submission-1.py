from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]

            res = float('inf')

            for coin in coins:
                res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        ans = dfs(amount)
        return -1 if ans == float('inf') else ans