class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) != m:
            nums1.pop()
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        
        
"""
.pop(): 指定した位置の要素を削除し、値を取得
.append()  末尾に要素を追加
.sort()   昇順にソート
.sort(reverse=True)   降順にソート
"""
