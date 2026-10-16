class Solution:
    import heapq
    from collections import defaultdict
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''ALWAYS should prioritize doing the task with the highest # 
        left for an optimal solution --> heap?

        MAX heap, where each element is tuple with (tasks # left, task) ; 
        e.g. (3, "A")
        tasks = ["A","A","A","B","C"]

        [(3, "A"), (1, "B"), (1, "C")]
        "A" is top of heap 

        counter to keep track of the minimum number of cpu cycles, init to 0

        We process the top of the heap --> A, so now we increment counter by 1, 
        but also we pop the heap. now, we do NOT want to re-add it to the heap just yet bc of the cooldown

        # add "A" to hashmap mapped to a tuple of (cooldown #, (tasks # left, task))
        # in every subsequent iteration, we decrement all tuple[0]'s values by 1, and when they hit 0, we re-push tuple[1] into the heap. also delete this pair from map

        # alg 
        ------
        # create mapping of (freq, element) --> O(N) time O(K) space where k is # of total elements in our map
        # push these onto a heap, klogk time ; O(k) space
        # iterate through the k values in the heap and pop -- O(k)
            # add to map O(1), but then decremenet all values by 1 O(k)
            # re-push if any values hit 0 ; O(klogk)
        # total: O(k * k * klogk)
        '''
        cooldowns = deque()
        all_tasks = []


        heap = [(-freq, char) for char, freq in Counter(tasks).items()]

        heapq.heapify(heap)

        time = 0

        while heap or cooldowns:
            time += 1

            while cooldowns and time >= cooldowns[0][0]:
                heapq.heappush(heap, cooldowns.popleft()[1])


            if heap:
                freq, char = heapq.heappop(heap)
                freq = -freq
                if freq > 1:
                    if n == 0:
                        heapq.heappush(heap, (-(freq - 1), char))
                    else:
                        cooldowns.append( (time + n + 1, (-(freq -1), char))   ) 

             


    

        return time

        
