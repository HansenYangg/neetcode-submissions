class MinStack:
    
    def __init__(self):
        # initialize empty stack/array
        # initialize min heap
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # appends to stack via .append
        # ALSO push to heap
        self.stack.append(val)
        
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

        

    def pop(self) -> None:
        # removes top of element from stack via .pop()
    
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        # gets stack[-1]
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # return min heap[0]
        if self.minStack:
            return self.minStack[-1]
