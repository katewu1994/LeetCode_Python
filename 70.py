class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0
        for _ in range(n):
            a,b = a+b,a
        return a 