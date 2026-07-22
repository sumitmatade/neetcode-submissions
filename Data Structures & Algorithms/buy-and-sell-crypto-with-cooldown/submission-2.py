class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dictionary to cache results: (index, buying_state) -> max_profit
        dp = {}

        def dfs(i, buying):
            # Base Case: out of bounds
            if i >= len(prices):
                return 0
            
            # Return cached result if already computed
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Decision 1: Cooldown (skip today)
            cooldown = dfs(i + 1, buying)

            if buying:
                # Decision 2: Buy stock today
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Decision 2: Sell stock today (must skip next day due to cooldown)
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)