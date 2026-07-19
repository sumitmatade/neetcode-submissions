from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Using lru_cache to memoize the results of dfs(i)
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            
            return False
            
        return dfs(0)