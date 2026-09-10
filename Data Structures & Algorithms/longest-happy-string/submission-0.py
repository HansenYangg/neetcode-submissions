class Solution:
    import heapq
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
      
        '''
        max heap with (freq, letter), and we should (almost always) add the letter with the highest 
        remaining frequency to our result string

        only condition is: if the letter with the highest frequency already appears in the rightmost 2 positions, then adding a third would violate the substring condition, so we need to temporarily pop it off the heap, add the SECOND largest element, and then re-push onto our max heap. a bunch of edge cases to look out for (heap is only size 1, substring is not >= len 2)

        i think alphabetically sorting by ties is okay? but maybe should greedily take the letter that does NOT previously appear in the end of our result substring

        heap = (  (1, a), (1, b), (1, c))
        result = bababcabc -- good



        '''

        res, heap = "", []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            
            freq, letter = heapq.heappop(heap)
            freq = -freq

            if len(res) >= 2 and res[-2:] == letter * 2 and heap:
                second_freq, second_letter = heapq.heappop(heap)
                second_freq = -second_freq

                res += second_letter
                heapq.heappush(heap, (-freq, letter))
                if second_freq - 1 > 0:
                    heapq.heappush(heap, (-(second_freq - 1), second_letter))

            elif len(res) >= 2 and res[-2:] == letter * 2 and not heap:
                return res

            else:
                res += letter
                if freq - 1 > 0:
                    heapq.heappush(heap, (-(freq - 1), letter))


        return res

        