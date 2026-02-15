class MyQueue:

    def __init__(self):
        self.stPush = []
        self.stPop = []

    def push(self, x: int) -> None:
        self.stPush.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.stPop.pop()

    def peek(self) -> int:
        if len(self.stPop) == 0:
            while self.stPush:
                self.stPop.append(self.stPush.pop())
        return self.stPop[-1]

    def empty(self) -> bool:
        return len(self.stPop) + len(self.stPush) == 0