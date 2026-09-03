class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
            
        res, curr_max, m = [], float('-inf'), {}
        for i in range(k):
            if nums[i] > curr_max:
                curr_max = nums[i]
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        res.append(curr_max)

        for idx, num in enumerate(nums[k:], start=k):
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

            left = nums[idx - k]
            m[left] -= 1
            if m[left] == 0:
                del m[left]

            if curr_max in m and curr_max >= num:
                res.append(curr_max)

            elif curr_max not in m and curr_max > num:
                curr_max = max(m.keys())
                res.append(curr_max)
            else:
                res.append(num)
                curr_max = num

           # 4 cases
           # 1. curr_max still in m and is >= num, still append curr_max
           # 2. curr_max still in m and is < num, num is new curr_max, so append num and update
           # 3. curr_max is not in m but is > num, need to recalculate max
           # 4. curr_max is not in m but is < num, num is new curr_max, so append num and update
                
            
        return res


        
