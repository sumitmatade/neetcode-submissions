from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Initialize a DP array where LIS[i] represents the length 
        # of the longest increasing subsequence ending at index i.
        dp = [1] * len(nums)
        
        # Iteratively build up the solution
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        # The answer is the maximum value in our DP array
        return max(dp)