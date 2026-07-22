class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        # Cache dictionary: (i, j) -> number of distinct subsequences
        dp = {}

        def dfs(i, j):
            # Base Case 1: Successfully matched all characters of t
            if j == len(t):
                return 1
            # Base Case 2: Exhausted s without matching all of t
            if i == len(s):
                return 0

            # Return cached result if already computed
            if (i, j) in dp:
                return dp[(i, j)]

            # Decision 1: Skip current character in s
            res = dfs(i + 1, j)

            # Decision 2: Match current characters if s[i] == t[j]
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            # Store result in cache
            dp[(i, j)] = res
            return dp[(i, j)]

        return dfs(0, 0) 