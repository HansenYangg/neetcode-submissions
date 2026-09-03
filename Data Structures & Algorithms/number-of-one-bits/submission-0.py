class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in bin(n) if i == "1"])