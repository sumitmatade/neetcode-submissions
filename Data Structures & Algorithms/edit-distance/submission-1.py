class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}  # Cache: (i, j) -> min operations

        def dfs(i, j):
            # Base Cases
            if i == m:
                return n - j  # Insert remaining characters of word2
            if j == n:
                return m - i  # Delete remaining characters of word1

            # Return cached result if state (i, j) was already evaluated
            if (i, j) in dp:
                return dp[(i, j)]

            # Characters match, no operation needed
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                # Try all 3 operations: Delete, Insert, Replace
                delete_op = dfs(i + 1, j)
                insert_op = dfs(i, j + 1)
                replace_op = dfs(i + 1, j + 1)

                dp[(i, j)] = 1 + min(delete_op, insert_op, replace_op)

            return dp[(i, j)]

        return dfs(0, 0)