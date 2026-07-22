class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Fast exit if total lengths don't match
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j):
            # Base Case: Reached the end of both strings
            if i == len(s1) and j == len(s2):
                return True

            # Return cached result if state (i, j) was already evaluated
            if (i, j) in dp:
                return dp[(i, j)]

            # Choice 1: Match character from s1
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True

            # Choice 2: Match character from s2
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True

            # Cache negative result if no valid path exists from state (i, j)
            dp[(i, j)] = False
            return False

        return dfs(0, 0)