class Solution:
    def checkValidString(self, s: str) -> bool:
        

        stack = []

        jacks = deque()

        for idx, char in enumerate(s):

            if char == "*":
                jacks.append(idx)

            elif char == "(":
                stack.append((char, idx))

            else:
                if stack: 
                    stack.pop()
                elif not stack and jacks and jacks[0] < idx:
                    jacks.popleft()
                else:
                    return False
        if jacks:
            while stack and jacks and jacks[-1] > stack[-1][1]:
                stack.pop()
                jacks.pop()

        return len(stack) == 0
