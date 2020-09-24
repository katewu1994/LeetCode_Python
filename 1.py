class Solution:
    def twoSum(self, nums, target):
        h={};
        for i, num in enumerate(nums):
            n = target - num
            
            if n in h:
                return [h[n],i]
            else:
                h[num] = i  