class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        t = s.split()
        n = len(t)
        
        if (n > 0):
            return len(t[n-1])
        else:
            return 0