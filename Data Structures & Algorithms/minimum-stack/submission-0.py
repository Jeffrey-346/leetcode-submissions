class MinStack:

    def __init__(self):
        self.stack = []
        self.my_dict = {} # maps the minimum element for each size stack
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1 or self.my_dict[len(self.stack) - 1] > val:
            self.my_dict[len(self.stack)] = val
        else:
            self.my_dict[len(self.stack)] = self.my_dict[len(self.stack) - 1]
        

    def pop(self) -> None:
        del self.my_dict[len(self.stack)]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.my_dict[len(self.stack)]
        
