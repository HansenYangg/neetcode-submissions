class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''two pointers, i and j. 
        always maintain a hashmap of size k
        if exceeds size k, shrink 1 element from left and increment i pointer
        at every nums[j], see if nums[j] is in our map, and if the conditions from the problem are met, and
        return true if so

        return false if loop terminates


        '''
        i = 0
        m = {}
        for j in range(len(nums)):
            if nums[j] not in m:
                m[nums[j]] = j
                if len(m) > k:
                    m[nums[j]] -= nums[i]
                    i += 1
                    if m[nums[j]] == 0:
                        del m[nums[j]]
            else: 
                if m[nums[j]] != j and nums[m[nums[j]]] == nums[j] and abs(m[nums[j]] - j) <= k:
                    return True
                else:
                    m[nums[j]] = j
                

            

        return False
        # [(1,0), (1,3), (2, 1), (3, 2)]
