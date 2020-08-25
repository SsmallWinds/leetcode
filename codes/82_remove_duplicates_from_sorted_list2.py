"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

思路:
建立一个哨兵指针，方便处理初始化的情况
维护pre和cur指针，通过判断cur 是否等于 cur.next 判断当前值是否重复
如果重复，pre.next = cur.next 删除cur 否则pre.next = cur 
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
    res = ListNode(-1)
    pre = res
    pre.next = head
    cur = head

    while cur != None and cur.next != None:
        is_dup = False
        while cur.next != None and cur.val == cur.next.val:
            is_dup = True
            cur = cur.next

        if is_dup:
            pre.next = cur.next
        else:
            pre = pre.next
        cur = cur.next
    return res.next


if __name__ == "__main__":
    a=ListNode(1)
    a1=ListNode(1)
    a2=ListNode(3)
    a3=ListNode(3)
    a4=ListNode(4)
    a5=ListNode(5)
    a6=ListNode(6)
    a.next=a1
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a4.next=a5
    a5.next=a6
    print_node(remove_dup(a))
