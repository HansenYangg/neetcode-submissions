class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        one, two, three = 0, 1, 1
        for i in range(n - 2):
            three, two, one = three + two + one, three, two   
        print(one, two, three)
        return three 

        '''
        0 1 1 2 3 5
        '''