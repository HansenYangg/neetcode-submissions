class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            print(stack)
            if operation not in "+DC":
                stack.append(int(operation))
            if operation == "+" and len(stack) >= 2:
               
                stack.append(stack[-1] + stack[-2])

            if operation == "D" and stack:
                stack.append(stack[-1] * 2)

            if operation == "C" and stack:
                stack.pop()
        return sum(stack)