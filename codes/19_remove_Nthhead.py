'''
删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

思路

我们注意到这个问题可以容易地简化成另一个问题：
删除从列表开头数起的第 (L - n + 1)(L−n+1) 个结点，
其中 LL 是列表的长度。只要我们找到列表的长度 LL，这个问题就很容易解决。

如何只遍历一次链表找到倒数第n个节点？
快慢指针，快指针先走n步，慢指针再走，快指针走到头，慢指针即为倒数第n个点
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

def remove_n(node:LinkNode, n:int)->LinkNode:
    q=node
    l=node
    while n > 1:
        q = q.next
        n -= 1

    while q.next != None:
        l = l.next
        q = q.next

    if l == node:
        return node.next
    else:
        l.data = l.next.data
        l.next = l.next.next
        return node

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

    print_node(remove_n(a, 5))
    print_node(remove_n(a, 4))
    