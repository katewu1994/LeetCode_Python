class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low = 0
        high = int(x/2)
        
        while low < high :
            mid = int(low + (high - low +1)/2)
            sq = mid * mid
            if sq <= x:
                low = mid
            else:
                high = mid -1
                
        return low