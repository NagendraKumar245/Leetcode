class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        
        low=2
        high=x//2
        while low <= high:
            mid=(low+high)//2
            squared = mid*mid
            
            if squared == x:
                return mid
            elif squared > x:
                high = mid-1
            else:
                low = mid+1

        return high
