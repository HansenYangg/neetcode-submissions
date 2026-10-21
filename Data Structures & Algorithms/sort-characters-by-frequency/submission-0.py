class Solution:
    from collections import Counter
    import heapq

    def frequencySort(self, s: str) -> str:

        cnt = Counter(s)

        heap = []

        for char, freq in cnt.items():
            heapq.heappush(heap, (-freq, char))

        res = ""
        print(heap)
        while heap:
            freq, char = heapq.heappop(heap)
            freq = -freq
            res += char * freq

        return res

        
        

