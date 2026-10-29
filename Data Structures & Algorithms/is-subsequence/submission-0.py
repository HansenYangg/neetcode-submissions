class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False


        sIdx = tIdx = 0

        while sIdx < len(s) and tIdx < len(t):
            if sIdx == len(s):
                break

            if s[sIdx] == t[tIdx]:
                sIdx, tIdx = sIdx + 1, tIdx + 1
            else:
                tIdx += 1

        return sIdx == len(s)

            