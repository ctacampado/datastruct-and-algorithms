from linkedList import Node, LinkedList

def linkedListTest():
    print("Running Linked List Test...")
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    llist = LinkedList(node1)
    llist.addNode(node3)
    llist.addNode(node4)
    llist.addNode(node2)
    data = llist.returnLinkedListData()
    print(data)
    if(data == [1,3,4,2]): print("pass!")
    else: print("fail!")

def runTests():
    linkedListTest()

runTests()