class MyQueue:

    def __init__(self):
        self.stack = []
        self.rev = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.rev = self.stack[::-1]
        

    def pop(self) -> int:
        val = self.rev.pop()
        self.stack = self.rev[::-1]
        return val

    def peek(self) -> int:
        if self.stack:
          return self.stack[0]
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()