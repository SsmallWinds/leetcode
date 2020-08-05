"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

思路:
步数直接与链表数量取余解决重复的问题
"""

class LinkNode:
    def __init__(self, data, next=None):
        self.val=data
        self.next=next

def print_node(node:LinkNode) -> None:
    res=[]
    while node!=None:
        res.append(node.val)
        node=node.next
    print(res)

def rotate(node:LinkNode, k:int) -> LinkNode:
    def get_last(node):
        res = None
        count = 0
        while node is not None:
            if node.next is None:
                res = node
            node = node.next
            count += 1
        return count, res

    def get_n(node, n):
        while n > 1:
            node = node.next
            n -= 1
        return node
    res = None
    count, last = get_last(node)
    if count == 0:
        return node
    k = k % count
    if k == 0:
        return node
    n = get_n(node, count - k)
    res = n.next
    n.next = None
    last.next = node
    return res

if __name__ == "__main__":
    a=LinkNode(1)
    a1=LinkNode(2)
    a2=LinkNode(3)
    a3=LinkNode(4)
    a.next=a1
    a1.next=a2
    a2.next=a3
    node = rotate(a, 4)
    print_node(node)

