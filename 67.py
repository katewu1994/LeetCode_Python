class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
    
# int(a,2) 将二进制（string）转为十进制 
# 例 int（‘100’,2） = 4
# bin(a) 将数值a转化为二进制
# [2:] 删除bin值中的 "0b" 