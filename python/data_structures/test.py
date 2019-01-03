from linkedList import Node, LinkedList

def linkedListTest(ctr):
    print("Running Linked List Test...")
    testData = []
    initNode = Node(ctr)
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

def runTests():
    linkedListTest(31)

runTests()