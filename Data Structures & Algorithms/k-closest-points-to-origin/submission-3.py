class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x1, x2, y1, y2):
            return ((x1-x2)**2 + (y1 - y2)**2)

        heap = []
        for point in points:
            heapq.heappush(heap, (dist(point[0], 0, point[1], 0), point))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res