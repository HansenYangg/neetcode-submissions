class Solution:
    import heapq
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            if not heap or (abs(a - x) < abs(heap[0][1] - x)) or (abs(a - x) == abs(heap[0][1] - x) and a < heap[0][1]) :
                heapq.heappush(heap, (-abs(a - x), a))
                if len(heap) > k:
                    heapq.heappop(heap)
            elif len(heap) < k:
                heapq.heappush(heap, (-abs(a - x), a))
              
            
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return sorted(res)
            