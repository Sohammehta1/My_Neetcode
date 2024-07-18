class MinStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        min_ele = float('inf')
        for ele in self.stack:
            if ele != None:
                if ele < min_ele:
                    min_ele = ele
        return min_ele
        
