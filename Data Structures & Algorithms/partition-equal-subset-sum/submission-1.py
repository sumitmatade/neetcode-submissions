from typing import List
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
            
        # Using lru_cache to remember results for pairs of (i, target)
        @lru_cache(None)
        def dfs(i, target):
            # Base case: if we exactly hit the target sum, we found a match
            if target == 0:
                return True
            # Base case: if out of bounds or target goes negative, it's invalid
            if i >= len(nums) or target < 0:
                return False
                
            # Choice 1: Skip the current number OR Choice 2: Include the current number
            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            
        return dfs(0, sum(nums) // 2)