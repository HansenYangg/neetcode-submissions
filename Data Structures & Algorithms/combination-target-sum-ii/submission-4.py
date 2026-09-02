class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(candidates, curr_arr, curr_val, i):
            nonlocal res
            if curr_val == target:
                res.append(curr_arr.copy())
                return

            if curr_val > target:
                return 
            
            for indx, num in enumerate(candidates[i:], start=i):
                if indx > i and candidates[indx] == candidates[indx - 1]:
                    continue
                backtrack(candidates, curr_arr + [num], curr_val + num, indx + 1)

        backtrack(candidates, [], 0, 0)
        return res