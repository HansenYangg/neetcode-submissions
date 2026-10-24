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
        
        maxOpen, minOpen = 0, 0


        for char in s:
            if maxOpen < 0:
                return False

            if char == "(":
                minOpen, maxOpen = minOpen + 1, maxOpen + 1

            elif char == ")":
                minOpen, maxOpen = minOpen - 1, maxOpen - 1
                if minOpen < 0:
                    minOpen = 0

            else:
                if minOpen > 0:
                    minOpen, maxOpen = minOpen - 1, maxOpen + 1
                else:
                    maxOpen = maxOpen + 1

        return minOpen == 0


            


            

        