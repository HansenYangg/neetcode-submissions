class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        
        m = "/-+*"
        stack, res = [], 0
        for token in tokens:
            if token in m and len(stack) >= 2:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "/" and num1 != 0:
                    res = int(num2 / num1)
                    stack.append(int(num2 /num1))
                
                elif token == "*":
                    res = num2 * num1
                    stack.append(num1 * num2)
                elif token == "-":
                    res = num2 - num1
                    stack.append(num2 - num1)
                elif token == "+":
                    res = num1 + num2
                    stack.append(num1 + num2)
            else:
                if token not in m:
                    stack.append(int(token))

        # [9, 4]
        # res = 3
        return res


            

            
