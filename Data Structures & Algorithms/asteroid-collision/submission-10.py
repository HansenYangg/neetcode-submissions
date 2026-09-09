class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            
            if not stack or (asteroid > 0 and stack[-1] > 0) or (asteroid < 0 and stack[-1] < 0) or (asteroid > 0 and stack[-1] < 0):
                stack.append(asteroid)
                
            else:
                case2 = False
                while stack and asteroid < 0 and stack[-1] > 0:
                    if abs(asteroid) == abs(stack[-1]): #equal, just discard from top of stack
                        stack.pop()
                        case2 = False
                        break
                        
                    
                    elif abs(stack[-1]) > abs(asteroid): # if top of stack is bigger, just discard current asteroid
                        case2 = False
                        break

                    elif abs(asteroid) > abs(stack[-1]): # current asteroid is bigger, so need to remove top of stack and potentially append to end of stack, but need to perform more iterations to see if there are more collisions   
                        case2 = True
                        stack.pop()

                if case2:
                    stack.append(asteroid)

                   
                
            
                    
        return stack

        # [2, 4,]