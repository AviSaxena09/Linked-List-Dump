# Node class
class Node:

    # initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None
    # Function to reverse the linked list
    def reverse(self): # Question a)
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    

    # Recursion Function
    def reverseRecusion(self, curr, prev):  # Question b) using recursion
        # If last node mark it head
        if curr.next is None:
            self.head = curr
            # Update next to prev node
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseFunc(next, curr)
        #This func calls the main reverse function 

    def reverse_recursive(self):
        if self.head is None:
            return
        self.reverseFunc(self.head, None)
    
    def reverseStack(self):  # Question c) using Stack
        # Stack initialization
        stk = [] 
        # Push the elements of list to stack  
        ptr = self.head  
        while ptr.next != None:  
            stk.append(ptr)  
            ptr = ptr.next
        # Pop from stack and replace  
        # current nodes value'  
        self.head = ptr  
        while len(stk) != 0:  
            ptr.next = stk.pop()  
            ptr = ptr.next
        ptr.next = None

    # insert a new node
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #  print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end = '=>')
            temp = temp.next
        print(" NONE")


# Calling of Respective Function
llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist2 = llist3 = llist

print("Given Linked List")
llist.printList()
print("\na : Reversed Linked List")
llist.reverse()
llist.printList()
print("\nb : Reversed Linked List using Recursion")
llist2.reverseRecusion
llist2.printList()
print("\nc : Reversed Linked List using Stack")
llist3.reverseStack
llist3.printList()
