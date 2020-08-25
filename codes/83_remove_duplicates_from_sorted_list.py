"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
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


def remove_dup(head:ListNode) -> ListNode:
    res = ListNode(None)
    cur = head
    pre = res

    while cur != None:
        if cur.val != pre.val:
            pre.next = cur
            pre = pre.next
        cur = cur.next
    # 最后的节点可能重复，需要截断
    pre.next = None
    return res.next

if __name__ == "__main__":
    a=ListNode(1)
    a1=ListNode(1)
    a2=ListNode(2)
    a3=ListNode(3)
    a4=ListNode(3)
    a5=ListNode(3)
    a6=ListNode(3)
    a.next=a1
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5
    a5.next=a6
    print_node(remove_dup(a))