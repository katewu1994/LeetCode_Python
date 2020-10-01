class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        front = 0
        back = len(needle)
        while front <= len(haystack) - len(needle):
            key = haystack[front:front+back]
            if key == needle:
                return front
            front += 1
        return -1