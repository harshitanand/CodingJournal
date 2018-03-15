'''
    Search an element in a Linked List (Iterative and Recursive)

    Write a function that searches a given key x in a given singly linked list. The function should return true if x is present in linked list and false otherwise.

        def search(Node *head, int x)  OR bool search(Node *head, int x)

    For example, if the key to be searched is 15 and linked list is 14->21->11->30->10, 
    then function should return false. If key to be searched is 14, then the function should return true.
'''

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

    def searchKey(self, key):
        ptr = self.head
        node_count = 1

        while ptr != None:
            if ptr.data == key:
                return True, node_count

            node_count += 1
            ptr = ptr.next

        return False, node_count

    def searchKeyRecursive(self, ptr, key):
        if ptr == None:
            return False
        elif ptr.data == key:
            return True

        return self.searchKeyRecursive(ptr.next, key)

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

    print '*********** Search ************'
    key = 10
    found, index = linkedList.searchKey(key)
    if found:
        print "{} is found at {} node in linked list".format(str(key), str(index))
    else:
        print "{} is not found in entire linked list".format(str(key))

    print '*********** Search Recursive ************'
    found = linkedList.searchKeyRecursive(linkedList.head, key)
    if found:
        print "{} is found in linked list".format(str(key))
    else:
        print "{} is not found in entire linked list".format(str(key))