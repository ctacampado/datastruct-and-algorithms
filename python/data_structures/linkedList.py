class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node
    
    def addNode(self, node):
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = node
    
    def returnLinkedListData(self):
        dataList = []
        curr = self.head
        while(curr.next != None):
            dataList.append(curr.data)
            curr = curr.next
        dataList.append(curr.data)
        return dataList
        


