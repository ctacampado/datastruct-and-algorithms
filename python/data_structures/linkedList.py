class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

    def insertNode(self, node, pos):
        if(pos > self.len or pos < 0):
            return -1
        else:
            print(self.len)
            curr = self.head
            prev = self.head
            if(pos == 0):
                self.head = node
                node.next = curr
            elif(pos == self.len):
                self.tail.next = node
                self.tail = node
            else:
                for i in range(pos):
                    prev = curr
                    curr = curr.next
                prev.next = node
                node.next = curr
            self.len += 1
    
    def deleteNode(self, pos):
        if(pos > self.len or pos < 0):
            return -1
        else:
            if(pos == 0):
                curr = self.head
                self.head = curr.next
            else:
                curr = self.head
                prev = self.head
                for i in range(pos):
                    if(i == pos-1):
                        prev = curr
                    curr = curr.next
                prev.next = curr.next
            self.len -= 1
    
    def data(self):
        dataList = []
        curr = self.head
        while(curr.next != None):
            dataList.append(curr.data)
            curr = curr.next
        dataList.append(curr.data)
        return dataList
        


