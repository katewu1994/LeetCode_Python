class Solution:
    from typing import List
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        l = min(len(x) for x in strs)
        lcp = strs[0][:l]
        for i in range(len(strs)):
            while l >= 0 and lcp != strs[i][:l]:
                l -= 1
                lcp = strs[0][:l]
        return lcp