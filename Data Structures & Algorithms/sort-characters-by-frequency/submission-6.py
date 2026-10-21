class Solution:
    from collections import Counter
    import heapq

    def frequencySort(self, s: str) -> str:
        '''
        know there are <= len(s) unique chars

        can use len(s) # of buckets, and use counter to get the mappings of each char to its freq

        iterate through this counter, and append the character * its frequency to the bucket of its corresponding frequency

        at the end, can iterate backwards from the buckets (bc higher freq will be at the end), and build up our returned string that way

        s = "tree"
        e:2
        t:1
        r:1

        [ [r, t], [ee], [], []. ]
        '''

        cnt = Counter(s)

        buckets = [ "" for _ in range(len(s)) ] 

        for char, freq in cnt.items():   
            buckets[freq - 1] += char * freq

        res = ""

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                res += buckets[i]
        
        return res

        
        

