# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low= 1
        high= n
        ans= 1
        
        while low<=high:
            mid = (low+high)//2
            if isBadVersion(mid) == False:
                low = mid+1
            else:
                high = mid-1
                ans = mid
                
        return ans    