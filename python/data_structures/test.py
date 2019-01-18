from linkedList import Node, LinkedList
from stack import Stack

def linkedListTest(ctr, pos):
    print("Running Linked List Test...")
    testData = []
    initNode = Node(ctr)
    print("test case 1: create a link list with", ctr, "node(s)")
    llist = LinkedList(initNode)
    testData.append(initNode.data)
    for i in range(ctr):
        llist.addNode(Node(i))
        testData.append(Node(i).data)
    data = llist.data()
    print("linked list length: ", llist.len)
    print(data)
    if(data == testData and llist.len == len(testData)): print("pass!")
    else: print("fail!")
    print("test case 2: insert new node at position", pos)
    newNode = Node(ctr+1)
    llist.insertNode(newNode, pos)
    newData = llist.data()
    print(newData)
    if(newData[pos] == newNode.data): print("pass!")
    else: print("fail!")
    print("test case 3: delete node at position", pos)
    llist.deleteNode(pos)
    newData = llist.data()
    print(newData)
    if(newData == testData and llist.len == len(testData)): print("pass!")
    else: print("fail!")

def stackTest():
    print("Running Stack Test...")
    testData = [1, '0x00', 0, True]
    s = Stack()
    print("pushing 1...")
    s.push(1)
    print("pushing B...")
    s.push('B')
    print("pushing &...")
    s.push('&')
    print("current stack stats:")
    print("top: ", s.top())
    print("size: ", s.size)
    print("is empty: ", s.isEmpty)
    print("popping all data...")
    s.pop()
    s.pop()
    resData = []
    resData.append(s.pop())
    resData.append(s.top())
    resData.append(s.size)
    resData.append(s.isEmpty)
    if(resData == testData):
        print("test data: ", testData)
        print("result data: ", resData)
        print("pass!")

def runTests():
    linkedListTest(0,0)
    linkedListTest(1,1)
    linkedListTest(3,2)
    linkedListTest(5,6)
    stackTest()

runTests()
