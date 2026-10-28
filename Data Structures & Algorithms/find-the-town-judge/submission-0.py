class Solution:

    from collections import defaultdict

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        1: [3]
        2: [3]
        3: [1, 2]

        people 1 to n
        two criteria for there to be a valid town judge: 
        1. there is one missing missing (e.g. len(keys) in our map is < n)
        2. this missing person is in every other person's 



        '''

        mapping = defaultdict(set)
        for a, b in trust:
            mapping[a].add(b)

        candidate = None
        for i in range(1, n + 1):
            if i not in mapping:
                candidate = i
                break

        if not candidate:
            return -1

        for a, b in mapping.items():
            if candidate not in b:
                return -1

        return candidate