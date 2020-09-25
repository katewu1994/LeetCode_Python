class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            s = str(x)
            s = int(s[::-1])
            if (x == s):
                return True
            else:
                return False
        else:
            return False
