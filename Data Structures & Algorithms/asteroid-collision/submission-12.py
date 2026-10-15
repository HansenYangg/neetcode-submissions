class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            
            # stack doesn't exist or the asteroids will not collide, so just append curr asteroid
            if not stack or (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0 and asteroid < 0):
                stack.append(asteroid)
            
            else:
                append = True 
                while stack and stack[-1] > 0 and asteroid < 0: # while stack has elements and WILL collide
             
                    if abs(stack[-1]) == abs(asteroid): # if equal size, both get destroyed -> don't append asteroid and pop
                        stack.pop()
                        append = False
                        break
                    
                    else: # differing size
                        asteroid_size, stack_size = abs(asteroid), abs(stack[-1])
                        if stack_size < asteroid_size: # top of stack smaller, so pop off and break, then append curr
                            stack.pop()
                            
                        else:
                            append = False
                            break

                if append:
                    stack.append(asteroid)


        return stack