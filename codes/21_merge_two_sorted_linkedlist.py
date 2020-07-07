'''
合并两个有序链表
'''

class LinkNode:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

def print_node(node:LinkNode)->None:
    res=[]
    while node!=None:
        res.append(node.data)
        node=node.next
    print(res)

def merge(node1:LinkNode, node2:LinkNode)->LinkNode:
    res = LinkNode(-1)
    temp = res
    while node1 != None or node2 != None:
        if node1 == None:
            temp.next = node2
            node2 = node2.next
            temp = temp.next
            continue
        if node2 == None:
            temp.next = node1
            node1 = node1.next
            temp = temp.next
            continue
        
        if node1.data > node2.data:
            temp.next = node2
            node2 = node2.next
            temp = temp.next
        else:
            temp.next = node1
            node1 = node1.next
            temp = temp.next

    return res.next

if __name__ == "__main__":
    a=LinkNode(2)
    a1=LinkNode(3)
    a2=LinkNode(4)
    a3=LinkNode(5)
    a4=LinkNode(6)
    a.next=a1
    a1.next=a2
    a2.next=a3
    a3.next=a4

    b=LinkNode(1)
    b1=LinkNode(7)
    b2=LinkNode(8)
    b3=LinkNode(9)
    b4=LinkNode(10)
    b.next=b1
    b1.next=b2
    b2.next=b3
    b3.next=b4

    print_node(a)
    print_node(b)
    print_node(merge(a, b))