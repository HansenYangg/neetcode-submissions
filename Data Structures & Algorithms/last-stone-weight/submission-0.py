class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        # add all to a max heap
        # at each step, pop off top 2
        # if equal, then dont do anything (destroyed)
        # if x < y, then push onto heap the new weight y - x
        # else, nothing i assume
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        print(maxHeap)
        while len(maxHeap) > 1:
            stone2 = -heapq.heappop(maxHeap)
            stone1 = -heapq.heappop(maxHeap)
            print(stone1, stone2)
            if stone1 < stone2:
                heapq.heappush(maxHeap, -(stone2 - stone1))

        return -maxHeap[0] if len(maxHeap) else 0


