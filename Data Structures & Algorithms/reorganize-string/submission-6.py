class Solution:
    import heapq
    from collections import Counter
    def reorganizeString(self, s: str) -> str:
        ''' 
        prioritize placing a character with the highest frequency first
        since dealing with frequency, could use. a heap? --> max heap with tuples as elements
        with (frequency, character)

        have an empty string we build up, constantly adding the character with the highest  frequency to our result string. 

        few cases:
        1. highest frequency char is the most recent char in our result array, so we can't use it
            a. if there is another element remaining in heap, we can append that (2nd highest freq)
            b. if there is not, we return an empty string because we have an invalid string
        
        2. highest frequency char is not most recently used, so we can use it, then repush onto heap with (frequency - 1, char)
        

        '''
        heap = []
        cnt = Counter(s)
        res = ""

        for char, freq in cnt.items():
            heapq.heappush(heap, (-freq, char))

        while heap:
            freq, char = heapq.heappop(heap)
            
            if not res: # res doesn't exist
                res += char
                if freq + 1 != 0:
                    heapq.heappush(heap, (freq + 1, char))

            elif char == res[-1]: # res does exist and there's a duplicate character, so we need to use 2nd highest freq
                if not heap:
                    return ""
                freq2, char2 = heapq.heappop(heap)
                res += char2
                if freq2 + 1 != 0:
                    heapq.heappush(heap, (freq2 + 1, char2))
                heapq.heappush(heap, (freq, char))

            else: # res does exist and there's not a duplicate character 
                res += char
                if freq + 1 != 0:
                    heapq.heappush(heap, (freq + 1, char))


        return res 

        

        


