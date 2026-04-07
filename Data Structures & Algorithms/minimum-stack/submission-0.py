class MinStack:

    def __init__(self):
        self.mintracker=[]
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.mintracker) == 0:
            self.mintracker.append(val)
        else:
            self.mintracker.append(min(self.mintracker[-1],val))
        

    def pop(self) -> None:
        self.arr.pop()
        self.mintracker.pop()
        

    def top(self) -> int:
        return self.arr[-1] if len(self.arr) > 0 else None
        
    def getMin(self) -> int:
        return self.mintracker[-1] if len(self.mintracker) > 0 else None
