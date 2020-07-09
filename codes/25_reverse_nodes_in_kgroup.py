'''
题目描述
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例:

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

思路：
按k的长度，反转子链表
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

def reverse(node:LinkNode, end:LinkNode)->LinkNode:
    pre = None
    next = None
    res = None
    head = node

    while node != end:
        next = node.next
        if next == end:
            res = node
        # 只管将当前节点指向pre
        node.next = pre
        pre = node
        node = next
    head.next = end
    return res

def swap_k(node:LinkNode, k:int)->LinkNode:
    head = node
    tail = node
    res = None
    pre_tail = None

    while tail != None:
        l = k
        while l > 0 and tail != None:
            l -= 1
            tail = tail.next
        pre_temp = head
        temp = reverse(head, tail)
        if res == None:
            res = temp
        head = tail
        if pre_tail != None:
            pre_tail.next = temp
        pre_tail = pre_temp
    return res

if __name__ == "__main__":
    a=LinkNode(2)
    a1=LinkNode(3)
    a2=LinkNode(4)
    a3=LinkNode(5)
    a4=LinkNode(6)
    a5=LinkNode(7)
    a.next=a1
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5

    print_node(swap_k(a, 2))