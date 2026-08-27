class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window of len(s1) within s2
        # maintain hashmap of the elements in both, comparing at each step
        # return true if matching hashmaps
        if len(s2) < len(s1):
            return False

        s1Map = Counter(s1)
        s2Map = Counter(s2[:len(s1)])

        if s2Map == s1Map:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            char = s2[r]
            if char in s2Map:
                s2Map[char] += 1
            else:
                s2Map[char] = 1

            left_char = s2[l]
            s2Map[left_char] -= 1
            if s2Map[left_char] == 0:
                del s2Map[left_char]
            l += 1

            if s2Map == s1Map:
                return True

                
        return False
            



