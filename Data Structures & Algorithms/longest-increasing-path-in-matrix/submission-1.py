class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # Cache: (r, c) -> longest path starting at (r, c)

        def dfs(r, c, prevVal):
            # Base Case: Out of bounds or not strictly increasing
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                matrix[r][c] <= prevVal):
                return 0
            
            # Return cached result if already computed
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            # Explore 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            # Cache the result for cell (r, c)
            dp[(r, c)] = res
            return res

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float('-inf')))
                
        return LIP