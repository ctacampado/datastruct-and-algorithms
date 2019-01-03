class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head  = node
        self.tail  = node
        self.len = 1
    
    def addNode(self, node):
        curr = self.head
        if(self.tail == curr):
            curr.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.len += 1

    def insertNode(self, node, p):
        pos = p-1
        if(pos >= self.len or pos <= 0):
            return -1
        else:
            curr = self.head
            for i in range(pos):
                curr = curr.next
            prev = curr.next
            curr.next = node
            node.next = prev
            self.len += 1
    
    def data(self):
        dataList = []
        curr = self.head
        while(curr.next != None):
            dataList.append(curr.data)
            curr = curr.next
        dataList.append(curr.data)
        return dataList
        


