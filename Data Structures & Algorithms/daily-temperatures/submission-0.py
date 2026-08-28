class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res array of just 0's * len(temp) // # [0, 0, 0, 0] for n =4
        # have a stack maintaining all of the indices of unresolved days
            # unresolved as in stil needs to find future warmer day

        # iterate through. at each index, compare if the val at top of stack is colder. if it is, we resolved this and found the next warmer day
            # update res array by curr index - index of the day we just resolved. continue looping until the top of stack is no longer cooler
        # need to track indices as well since that is what we are storing in res array 
        # [1, 0, 1, 2, 1, 0, 0]
        # stack = [40]

        res = [0] * len(temperatures)
        stack = []
        for indx, temp in enumerate(temperatures):
            if not stack:
                stack.append(indx)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    i = stack.pop()
                    res[i] = indx - i
                stack.append(indx)

        return res
