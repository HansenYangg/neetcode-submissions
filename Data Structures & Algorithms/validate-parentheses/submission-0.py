class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")": "(", "}": "{", "]": "["}

        for string in s:
            if string not in m:
                stack.append(string)
            else: #is a closing bracket
                if not stack or m[string] != stack.pop():
                    return False


        return len(stack) == 0