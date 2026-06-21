class MinStack(object):

    def __init__(self):
        self.stack=[]        
        self.minstack=[]
    def push(self, value):
        self.stack.append(value)
        if len(self.minstack)==0:
            self.minstack.append(value)
        else:
            if self.stack[-1]<=self.minstack[-1]:
                self.minstack.append(value)

    def pop(self):
        y=self.stack.pop()
        if y == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()