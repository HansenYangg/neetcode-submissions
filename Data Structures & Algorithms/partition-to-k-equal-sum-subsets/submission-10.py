class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        used, target_sum = [False] * len(nums), sum(nums) // k
        nums.sort(reverse=True)

        def backtrack(curr_sum, k, i):
             
                if k == 0:
                    return True
                if curr_sum == target_sum:
                    return backtrack(0, k - 1, 0)
                 

                for idx in range(i, len(nums)):
                    val = nums[idx]
                    if used[idx] == False and val + curr_sum <= target_sum:
                        used[idx] = True
                        if backtrack(curr_sum + val, k, idx + 1):
                            return True
                        used[idx] = False

                   

                return False
                        

        
        return backtrack(0, k, 0)
            