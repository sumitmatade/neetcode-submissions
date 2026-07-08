class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix:
                count += prefix[prefix_sum - k]

            prefix[prefix_sum] = prefix.get(prefix_sum, 0) + 1

        return count