class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundary padding of 1s
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            # Base Case: no balloons between l and r
            if l > r:
                return 0

            # Return cached result if already computed
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            # Try making each balloon i the LAST one to burst in interval [l, r]
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                # Fixed: use 'l' (letter l) instead of '1' (number 1)
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)