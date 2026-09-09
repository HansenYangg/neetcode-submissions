class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = min(strs, key=len)
        for string in strs:
            while string[:len(res)] != res:
                res = res[:-1]
                if not res:
                    break


        return res