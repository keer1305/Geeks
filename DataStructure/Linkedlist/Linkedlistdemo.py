class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def _init_(self):
        self.head=None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next


list=LinkedList()
list.head=Node("ONE")
c2=Node("TWO")
c3=Node("THREE")

list.head.next=c2
c2.next=c3

list.printlist()
