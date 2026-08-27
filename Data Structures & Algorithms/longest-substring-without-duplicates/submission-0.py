class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        curr, res = 0, 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[l])
                l += 1
                curr -= 1


            sett.add(s[right])
            curr += 1

            res = max(res, curr)
        return res
        