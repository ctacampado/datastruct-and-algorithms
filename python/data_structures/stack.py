from linkedList import Node

class Stack:
    def __init__(self):
        self.t = None
        self.size = 0
        self.isEmpty = True
    
    def push(self, data):
        n = Node(data)
        if(None == self.t):
            self.t = n
        else:
            n.prev = self.t
            self.t.next = n
            self.t = n
        self.isEmpty = False
        self.size += 1

    def pop(self):
        if(0 == self.size):
            return '0x00'
        else:
            val = self.t.data
            if(self.t.prev != None):
                self.t = self.t.prev
                self.t.next = None
            else:
                self.t = None

            self.size -= 1
            if(0 == self.size):
                self.isEmpty = True
            return val

    def top(self):
        if(0 == self.size):
            return '0x00'
        else:
            return self.t.data