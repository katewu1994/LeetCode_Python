class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        current = 0
        
        for n in nums:
            if current < 0:
                current = 0
            current = current + n
            maxsub = max(maxsub,current)
            
        return maxsub