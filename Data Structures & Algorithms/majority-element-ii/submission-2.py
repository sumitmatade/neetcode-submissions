import collections

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Count the frequency of each number in the array
        counts = collections.Counter(nums)
        
        # Calculate the threshold
        threshold = len(nums) // 3
        
        # Return a list of all numbers that exceed the threshold
        return [num for num, count in counts.items() if count > threshold]