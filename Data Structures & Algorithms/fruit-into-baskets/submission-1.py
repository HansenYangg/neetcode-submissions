class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit1, fruit2 = None, None
        m = {}
        res = curr = l = 0
        for i in range(len(fruits)):
            if fruit1 == None and fruit2 == None: # both are none
                fruit1 = fruits[i]
                m[fruits[i]] = 1
                curr += 1

            elif fruit1 != None and fruit2 == None or fruit1 == None and fruit2 != None: # one open basket, new fruit 
                if fruits[i] != fruit1:
                    fruit2 = fruits[i]
                    m[fruits[i]] = 1
                else:
                    m[fruits[i]] += 1
                curr += 1

            elif fruits[i] == fruit1 or fruits[i] == fruit2: # both baskets taken but is a duplicate fruit
                m[fruits[i]] += 1
                curr += 1

            else:
                while l < len(fruits): # both baskets taken but new fruit 
                    
                    m[fruits[l]] -= 1
                    curr -= 1
                    if m[fruits[l]] == 0:
                        del m[fruits[l]]
                        if fruit1 == fruits[l]:
                            fruit1 = fruits[i]
                         
                        else:
                            fruit2 = fruits[i]

                        m[fruits[i]] = 1
                        curr += 1
                        l += 1
                        break
                    
                    
                    l += 1
                    
                        
                        
            res = max(res, curr)
            
        return res
