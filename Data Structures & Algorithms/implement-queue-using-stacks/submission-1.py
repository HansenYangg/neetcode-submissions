class MyQueue:

    def __init__(self):
        self.q1, self.q2 = [], []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.q1:
            while self.q1:
                self.q2.append(self.q1.pop())
            res = self.q2.pop()

            while self.q2:
                self.q1.append(self.q2.pop())

            return res

# [1, 2, 3]
# [3,]

    def peek(self) -> int:
        if self.q1:
            while self.q1:
                self.q2.append(self.q1.pop())
            res = self.q2[-1]

            while self.q2:
                self.q1.append(self.q2.pop())

            return res


        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()