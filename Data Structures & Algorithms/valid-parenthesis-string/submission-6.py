class Solution:
    def checkValidString(self, s: str) -> bool:
        '''

        stack approach, where if we ever find a left parenthesis, just append to the stack 
        have a separate queue for the stars, keeping track of their indices

        if we ever encounter a closing parenthesis, we see if the top of the stack has a corresponding opening parenthesis. if it does, just pop from the stack

        if stack does not contain opening parenthesis, we see if their is a valid star that is LEFT of the the current indice we're on

        
        [ 0 ] 
        stars = [2, 3]


        '''
        stack = []
        stars = deque()

        for idx, el in enumerate(s):
            if el == "(":
                stack.append(idx)
            
            elif el == "*":
                stars.append(idx)

            else:
                if stack:
                    stack.pop()
                elif not stars or stars[0] > idx: 
                    return False

                else:
                    stars.popleft()

        while stack:
            if not stars or stars[-1] < stack[-1]:
                return False
            stars.pop()
            stack.pop()

        return True 
            


            

        