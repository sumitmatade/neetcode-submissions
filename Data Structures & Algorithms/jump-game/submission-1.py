from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Keep track of the maximum index we can reach so far
        max_reachable = 0
        
        for i in range(len(nums)):
            # If the current index is beyond the maximum we can reach,
            # it means we are stuck and can't move forward.
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach from the current position
            max_reachable = max(max_reachable, i + nums[i])
            
            # Optimization: If we can already reach or surpass the last index, return True early
            if max_reachable >= len(nums) - 1:
                return True
                
        return True