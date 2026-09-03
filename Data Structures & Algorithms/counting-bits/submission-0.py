class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(binary):
            res = 0
            while binary:
                res += binary & 1
                binary >>= 1
            return res

        res = []
        for num in range(0, n + 1):
            res.append(countOnes(num))

        return res
        