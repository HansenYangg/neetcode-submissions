class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map each element to freq (e.g. (int, freq)) --> (5, 3)
        # add these to a min heap, based on first element (freq)
            # whenever size exceeds k, shrink min heap
        # pop all remaining elements off min heap and just add the 1st elements to a return array
        m = Counter(nums) # O(N)
        
        heap = []
        for val, freq in m.items(): 
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
        


