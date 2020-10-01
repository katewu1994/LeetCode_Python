class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        a = 0
        b = len(nums)-1
        
        if nums[b] < target:
            return b+1

        while a <= b:
            mid =(a + b)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                b = mid - 1
            else:
                a = mid + 1
        
        return a