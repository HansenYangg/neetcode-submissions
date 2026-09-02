class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
       

        ''' iterate through s and add to our s_map if the current s[i] is in t
        and ONLY if s[i] is in t. at every iteration we increase curr by 1. also need to only increase s_map[s[right]] if it's < t_map[s[right]]


        if at any point s_map == t_map, we shrink our window size from the left until we encounter an element that IS in s, so we know to stop otherwise our substring will no longer be valid. we shrink our curr accordingly, then after this is done, we update res if curr < res

        need to handle what happens next? --> we already have a valid substring,
        but how do we proceed now?

        shrink window even more so that we DO remove an element from our s_map so it no longer == t_map, then continue with our loop


        '''

        res = ""
        lowest = float("inf")
        curr = left = 0
        t_map, s_map = Counter(t), Counter()
        need, have = len(t_map), 0

        for right in range(len(s)):
            curr += 1 

            if s[right] in t_map:
                if s[right] in s_map:
                    s_map[s[right]] += 1
                elif s[right] not in s_map:
                    s_map[s[right]] = 1
                    
                if s_map[s[right]] == t_map[s[right]]:
                    have += 1

            while have >= need:
                while s[left] not in s_map:
                    curr, left = curr - 1, left + 1

                if curr < lowest:
                    lowest = curr
                    res = s[left:right + 1]
                
                
                s_map[s[left]] -= 1

                if s_map[s[left]] == 0:
                    del s_map[s[left]]
                    have -= 1
                elif s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                curr, left = curr - 1, left + 1

               


        return res