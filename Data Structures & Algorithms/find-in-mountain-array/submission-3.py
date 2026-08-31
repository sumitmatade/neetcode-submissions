class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        # 1. Find the index of the peak element
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1 # Peak is to the right
            else:
                right = mid    # Peak is to the left or at mid
                
        peak = left
        
        # 2. Binary search on the ascending portion (left of peak)
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        # 3. Binary search on the descending portion (right of peak)
        left, right = peak + 1, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target: # Note: logic is flipped for descending array
                left = mid + 1
            else:
                right = mid - 1
                
        return -1