class Solution:
    from collections import Counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = Counter(nums)
        res = []
        s = set()
        def backtrack(curr, m, string, i):
            if len(curr) == len(nums):
                if string not in s:
                    res.append(curr.copy())
                    s.add(string)
                    return 
                return

            if i >= len(nums):
                return 

            for idx, val in enumerate(nums):
                if val in m:
                    if m[val] + 1 <= n[val]:
                        m[val] += 1
                        backtrack(curr + [val], m, string + str(val), idx)
                        m[val] -= 1
                else:
                    m[val] = 1
                    backtrack(curr + [val], m, string + str(val), idx)
                    del m[val]

        backtrack([], {}, "", 0)
        return res