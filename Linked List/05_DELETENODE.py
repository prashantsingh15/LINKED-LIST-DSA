from sys import stdin

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

def length(head):
    if head is None:
        return 0
    count=0

    while head is not None:
        count +=1
        head=head.next

    return count


def deleteNode(head,pos):
    if pos<0 or pos> (length(head)):
        return head

    if head is None:
        return head 

    if pos==0:
        return head.next

    c=0
    prev=None
    curr=head
    while c<pos:
        prev =curr
        curr=curr.next
        c +=1

    if prev is not None:
        prev.next=curr.next

    return head

        
        
        
        




















# Taking Input Using Fast I/O.
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


head=takeInput()
print(length(head))
head=deleteNode(head,2,6)
print(length(head))
head=deleteNode(head,0,9)
print(length(head))
head=deleteNode(head,7,10)
print(length(head))



# Main.
# t = int(stdin.readline().strip())

# while t > 0 :
    
#     head = takeInput()
#     pos = int(stdin.readline().rstrip())
    
#     head = deleteNode(head, pos)
#     printLinkedList(head)

#     t -= 1