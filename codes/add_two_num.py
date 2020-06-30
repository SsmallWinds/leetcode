'''
题目描述
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
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

def sum_node(node1:LinkNode, node2:LinkNode)->LinkNode:
    res=LinkNode(-1)
    temp=res
    carry=0
    while node1 != None or node2 != None:
        val1 = 0
        val2 = 0
        if node1 != None:
            val1=node1.data
            node1=node1.next
        if node2 != None:
            val2=node2.data
            node2=node2.next
        sum_val = val1 + val2 + carry
        carry=int(sum_val/10)
        temp.next=LinkNode(sum_val%10)
        temp=temp.next
    if carry != 0:
        temp.next=LinkNode(carry)
    return res.next

if __name__ == "__main__":
    a=LinkNode(2)
    a1=LinkNode(4)
    a2=LinkNode(3)
    a.next=a1
    a1.next=a2

    b=LinkNode(9)
    b1=LinkNode(6)
    b2=LinkNode(6)
    b.next=b1
    b1.next=b2

    print_node(a)
    print_node(b)
    print_node(sum_node(a,b))
    