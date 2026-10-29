class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr) 
        res[-1] = -1

        maxSeen = arr[-1]

        print(maxSeen)
        for i in range(len(arr) - 2, -1, -1):
         
            maxSeen = max(maxSeen, arr[i + 1])
            res[i] = maxSeen

        return res

