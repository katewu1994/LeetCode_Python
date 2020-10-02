class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = int(''.join(map(str,digits)))
        val = val +1
        ans = [int(i) for i in str(val)]
        return ans