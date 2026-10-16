class Solution:
    from collections import Counter
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        brute force: always start from min in array, remove the min, and continuously see if min + 1 in array till it reaches groupsize K // O(1) space, O(N*N*K)

        sort hand, maintain used set of indices
        iterate through hand till we form group size k, return false if we don't
        repeat for next smallest, nonused indice 


        '''
        if len(hand) % groupSize != 0:
            return False
        m = Counter(hand)
        hand.sort()
       

        for num in hand:
            if m[num] == 0:
                continue

            currGroup, currNum = 0, num
            while currGroup < groupSize:
                if currNum not in m or m[currNum] == 0:
                    return False

                m[currNum] -= 1
                currNum, currGroup = currNum + 1, currGroup + 1

            
           
            

                

        '''
        [(4, 4), (5, 4)]
        '''

        return True