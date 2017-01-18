'''
A Tale of Two Stacks


'''

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if len(self.second) == 0:
            while len(self.first) >0:
                self.second.append(self.first.pop())
        if len(self.second) == 0:
            return None
        return self.second[-1]

    def pop(self):
        if len(self.second) == 0:
            while len(self.first)>0:
                self.second.append(self.first.pop())
        if len(self.second) == 0:
            return None
        return self.second.pop()

    def put(self, value):
        self.first.append(value)



queue = MyQueue()
queue.put(42)
queue.pop()
queue.put(14)
print queue.peek()