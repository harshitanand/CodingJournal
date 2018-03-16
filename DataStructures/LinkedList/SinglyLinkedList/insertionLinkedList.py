class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, prev_node, value):
        if prev_node is None:
            print "The given previous node must inLinkedList."

        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while last.next != None:
            last = last.next

        last.next = new_node

    def printLinkedList(self):
        tmp = self.head

        while tmp != None:
            print "{} -->".format(str(tmp.data)),
            tmp = tmp.next

        print "None"

def init():
    llist = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head = first
    first.next = second
    second.next = third

    return llist

if __name__=='__main__':

    print '*********** Before Insertion ***********'
    linkedList = init()
    linkedList.printLinkedList()

    print '*********** Push **********'
    linkedList.push(5)
    linkedList.printLinkedList()

    print '*********** Insert After **********'
    linkedList.insertAfter(linkedList.head.next.next, 9)
    linkedList.printLinkedList()

    print '*********** Append ************'
    linkedList.append(10)
    linkedList.printLinkedList()

    