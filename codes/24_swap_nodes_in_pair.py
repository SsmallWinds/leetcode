'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''

from functools import total_ordering

@total_ordering
class LinkNode:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
    
    def __eq__(self, other):
        if self is None and other is not None:
            return False
        if self is not None and other is None:
            return False
        if self is None and other is None:
            return True
        return self.data == other.data

    def __le__(self, other):
        return self.data < other.data

def print_node(node:LinkNode)->None:
    res=[]
    while node!=None:
        res.append(node.data)
        node=node.next
    print(res)

def swap_pair(node:LinkNode)->LinkNode:
    res = LinkNode(-1)
    res.next = node
    temp = res

    while temp.next != None and temp.next.next != None:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
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

    print_node(swap_pair(a))