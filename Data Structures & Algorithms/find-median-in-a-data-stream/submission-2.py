class MedianFinder:
    import heapq

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    '''
    add 2, 1, 3, 4, 5, 6
    min = [1]
    max = [-7, -9]
    (1) all elements in minheap should be strictly < maxheap

    for addnum:
    if evenly lengthed:
        if num >= top of maxheap, add to maxheap and then pop off and add top of maxheap to minheap
        else:
            can just add just minheap reguarly


    else: odd length (max heap is larger)
        if num >= top of maxheap, add to maxheap and then pop off and add top of maxheap to minheap
        else: add to minheap
       

    for findmedian, if len is equal, then just return median of top of min heap + -top of max heap
    if len not equal, then return -top of maxheap


    '''
        

    def addNum(self, num: int) -> None:
        if not self.minheap and not self.maxheap:
            heapq.heappush(self.maxheap, -num)

        else:
            heapq.heappush(self.maxheap, -num)
            maxx = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, maxx)
            if len(self.minheap) - 2 == len(self.maxheap):
                minn = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -minn)

            



        
        

    def findMedian(self) -> float:
        if not self.minheap and not self.maxheap:
            return 0

        if self.minheap and self.maxheap:
            if len(self.minheap) == len(self.maxheap):
                return (self.minheap[0] + -self.maxheap[0]) / 2
            else:
                if len(self.minheap) > len(self.maxheap):
                    return self.minheap[0]
                return -self.maxheap[0]

        
        if self.minheap:
            return self.minheap[0]

        return -self.maxheap[0]
        
        
        