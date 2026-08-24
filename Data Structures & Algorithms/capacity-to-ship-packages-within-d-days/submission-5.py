class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Define the binary search boundaries
        left = max(weights)
        right = sum(weights)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Simulate shipping with 'mid' capacity
            ships = 1
            current_cap = mid
            
            for w in weights:
                if current_cap - w < 0:
                    ships += 1
                    current_cap = mid
                current_cap -= w
                
            # Adjust the search space
            if ships <= days:
                res = min(res, mid)
                right = mid - 1 # Try to find a smaller valid capacity
            else:
                left = mid + 1  # Capacity was too small, we need more
                
        return res