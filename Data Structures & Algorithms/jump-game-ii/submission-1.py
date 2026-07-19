from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the array has 1 or fewer elements, we are already at the end.
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        furthest_reachable = 0
        
        # We iterate up to len(nums) - 1 because once we reach the 
        # last index, we don't need to make another jump.
        for i in range(len(nums) - 1):
            # Keep track of the furthest index we can reach from the current window
            furthest_reachable = max(furthest_reachable, i + nums[i])
            
            # If we've reached the end of the range for the current jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = furthest_reachable
                
                # Early optimization: if we can already reach the last index, break out
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps