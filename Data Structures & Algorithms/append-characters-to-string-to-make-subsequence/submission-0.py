class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sIdx = tIdx = 0

        while sIdx < len(s) and tIdx < len(t):

            if s[sIdx] == t[tIdx]:
                sIdx, tIdx = sIdx + 1, tIdx + 1

            else:
                sIdx += 1

        return len(t) - tIdx