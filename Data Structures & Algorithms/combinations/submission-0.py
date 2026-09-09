class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(arr, i):
            if len(arr) == k:
                res.append(arr.copy())
                return

            if len(arr) > k:
                return 

            for i in range(i, n + 1):
                backtrack(arr + [i], i + 1)



        backtrack([], 1)
        return res