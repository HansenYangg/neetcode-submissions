class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        l, r, res = 0, len(people) - 1, 0
        people.sort()
        while l <= r:
            res += 1
            if people[l] + people[r] <= limit:
                l, r = l + 1, r - 1
            else:
                r -= 1


        return res