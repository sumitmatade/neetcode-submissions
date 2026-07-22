class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Cache dictionary: (index, remaining_amount) -> combinations_count
        memo = {}

        def dfs(i, a):
            # Base Case 1: Target amount reached
            if a == 0:
                return 1
            # Base Case 2: Out of bounds or amount went negative
            if i >= len(coins) or a < 0:
                return 0
            
            # Return cached result if already computed
            if (i, a) in memo:
                return memo[(i, a)]

            # Decision 1: Include current coin (stay at index i, reduce amount)
            # Decision 2: Exclude current coin (move to index i + 1, keep amount)
            memo[(i, a)] = dfs(i, a - coins[i]) + dfs(i + 1, a)
            
            return memo[(i, a)]

        return dfs(0, amount)