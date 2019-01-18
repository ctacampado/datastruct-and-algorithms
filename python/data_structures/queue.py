from linkedList import Node

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0
        self.isEmpty = True

    def enqueue(self, data):
        n = Node(data)
        if(None == self.rear):
            self.rear = n 
            self.front = n
        else:
            self.rear.prev = n
            self.rear = n
        self.size += 1
        self.isEmpty = True

    def dequeue(self):
        if(None != self.front):
            val = self.front.data
            if(None != self.front.prev):
                self.front = self.front.prev
            else:
                self.front = None
                self.rear = None
            self.size -= 1
            return val
        else:
            return '0x00'