class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends: 
            return -1

        mapping = {
                    "0": "19", 
                    "1": "02", 
                    "2": "13",
                    "3": "24",
                    "4": "35",
                    "5": "46",
                    "6": "57",
                    "7": "68",
                    "8": "79",
                    "9": "08"
                     
                     
                     }

       
        
        q = deque(["0000"])
        
        seen = set()
        seen.add("0000")

        

        res = 0
       
     
        while q:
            
            
            for _ in range(len(q)):
                curr = q.popleft()
               
                if curr == target:
                    return res

                options = []
                for idx, digit in enumerate(curr):
                    
                    options.append(curr[:idx] + mapping[digit][0] + curr[idx + 1:])
                    options.append(curr[:idx] + mapping[digit][1] + curr[idx + 1:])

                for option in options:
                    if option not in deadends and option not in seen:
                        q.append(option)
                        seen.add(option)


            res += 1
                    

                


        return -1






