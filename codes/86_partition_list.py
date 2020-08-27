"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

简单的链表操作，遍历链表分组，再拼接时间复杂度为O(n)
"""

class ListNode:
    def __init__(self, val=None, next=None):
        self.val=val
        self.next=next

def print_node(node:ListNode)->None:
    res=[]
    while node!=None:
        res.append(node.val)
        node=node.next
    print(res)

def gen_list(s:str) -> ListNode:
    head = ListNode(-1)
    cur = head
    items = s.split('->')
    for item in items:
        cur.next = ListNode(int(item))
        cur = cur.next
    return head.next

def partition(head:ListNode, x:int) -> ListNode:
    left = ListNode(-1)
    left_cur = left
    right = ListNode(-1)
    right_cur = right
    cur = head
    
    while cur != None:
        if cur.val < x:
            left_cur.next = cur
            left_cur = left_cur.next
        else:
            right_cur.next = cur
            right_cur = right_cur.next
        cur = cur.next
    left_cur.next = right.next
    right_cur.next = None
    return left.next


if __name__ == "__main__":
    list = gen_list('1->4->3->2->5->2')
    print_node(partition(list, 3))