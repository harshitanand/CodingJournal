class Node:

    def __init__(self, data):
        self.data = data;
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

def init():
    llist = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head = first
    first.next = second
    second.next = third

    return llist

def printLinkedList(linkedList):
    tmp = linkedList.head

    while tmp != None:
        print "{} -->".format(str(tmp.data)),
        tmp = tmp.next

    print "None"

if __name__=='__main__':
    
    linkedList = init()
    printLinkedList(linkedList)

    
