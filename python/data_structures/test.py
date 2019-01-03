from linkedList import Node, LinkedList

def linkedListTest(ctr, pos):
    print("Running Linked List Test...")
    testData = []
    initNode = Node(ctr)
    print("test case 1: create a link list with", ctr, "nodes")
    llist = LinkedList(initNode)
    testData.append(initNode.data)
    for i in range(ctr-1):
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
    if(newData[pos] == newNode.data and llist.len == len(testData)+1): print("pass!")
    else: print("fail!")

def runTests():
    linkedListTest(31,3)

runTests()
