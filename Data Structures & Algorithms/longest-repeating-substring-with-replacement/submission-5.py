class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A:4, B:2, 
        # iterate through s, adding each element to a counter
        # if at any point, if sum(map.keys()) - max(map.keys()) > k, need to 
        # trim from the left
            # in order to save time recomputing, can instead keep track of curr sum and max
        
        res, currMax, currSum, left, m = 0, 0, 0, 0, {}
        for right in range(len(s)):
            if s[right] in m:
                m[s[right]] += 1
            else:
                m[s[right]] = 1
            currMax += 1
            currSum += 1

            while currSum - max(m.values()) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                currMax -= 1
                currSum -= 1
                left += 1


            res = max(res, currMax)
        return res


