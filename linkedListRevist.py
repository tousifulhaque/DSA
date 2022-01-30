class Node:
    # data contains the value of the node
    # next is the  full next node
    def __init__(self,data, next):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self, node = None):
        self.head = node
    
    def insert_at_begining(self, data):
        self.head = Node(data, self.head)
    
    def print_ll(self):
        itr = self.head
        while itr != None:
            print(str(itr.data) + '---->')
            itr = itr.next


ll = LinkedList()
ll.insert_at_begining(64)
ll.insert_at_begining(85)

ll.print_ll()