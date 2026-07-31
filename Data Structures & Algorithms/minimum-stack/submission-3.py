class MinStack:

    def __init__(self):
        self.Minstack=[]
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.Minstack:
            val=min(self.Minstack[-1],val) 
        self.Minstack.append(val)
    def pop(self) -> None:
        self.Minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Minstack[-1]
