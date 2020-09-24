class Solution:
    def reverse(self, x: int) -> int:
        if (-2**31 <= x <= 2**31 - 1):
            s = str(x)
            if x >= 0:
                s = s[::-1]
                s = int(s)
                if (s > 2**31 - 1):
                    s = 0
                return s
            
            else:
                x = -x
                s = str(x)
                s = s[::-1]
                s = -int(s)
                if (s < -2**31):
                    s = 0
                return s
        
        else:
            s = 0
            return s
        