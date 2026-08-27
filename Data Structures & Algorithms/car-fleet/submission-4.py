class Solution:
    import math
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # compute sorted order, nested list with each sublist being [pos, speed]
        # compute arrival times
        # initialize num fleets to 0
        # iterate through each arrival time, if prev car < ahead car arrival time, can add it to fleet
        # else, will arrive in a different fleet

        #return calculated num fleets
        if not position:
            return 0

        sort = sorted([[position[i], speed[i]] for i in range(len(position))], reverse=True)
        arrival_times = [(target - pair[0]) / pair[1] for pair in sort]

        fleets, indx = 0, 0
        while indx < len(position):
            curr_car, fleets = arrival_times[indx], fleets + 1
            while indx < len(position) - 1 and arrival_times[indx + 1] <= curr_car:
                indx += 1
            indx += 1


        return fleets



