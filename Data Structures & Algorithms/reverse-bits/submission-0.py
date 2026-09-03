class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        for i in range(32):
            res += str(n & 1)
            n >>= 1
    
        return int(res, 2)
        
