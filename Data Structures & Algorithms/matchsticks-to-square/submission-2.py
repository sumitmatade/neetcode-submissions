class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        
        # If the total sum isn't divisible by 4, a square is impossible
        if total_sum % 4 != 0:
            return False
            
        target = total_sum // 4
        
        # Optimization 1: Sort descending to fail faster
        matchsticks.sort(reverse=True)
        
        sides = [0] * 4

        def dfs(i):
            # If we reach the end, we successfully placed everything
            if i == len(matchsticks):
                return True 

            for side in range(4):
                # Optimization 2: Only add if it doesn't exceed the target length
                if sides[side] + matchsticks[i] <= target:
                    sides[side] += matchsticks[i]
                    
                    if dfs(i + 1):
                        return True
                        
                    sides[side] -= matchsticks[i] # Backtrack
                    
                    # Optimization 3: If placing in an empty side failed, 
                    # placing it in another empty side will also fail.
                    if sides[side] == 0:
                        break

            return False

        return dfs(0)