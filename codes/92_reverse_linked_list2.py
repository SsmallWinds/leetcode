"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_node(node: ListNode, remark='') -> None:
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    print(remark, res)


def gen_list(s: str) -> ListNode:
    head = ListNode(-1)
    cur = head
    items = s.split('->')
    for item in items:
        cur.next = ListNode(int(item))
        cur = cur.next
    return head.next


def reverse(header: ListNode, m: int, n: int) -> ListNode:
    if m == n:
        return header
    cur = header
    dummy = ListNode(-1)
    dummy.next = cur
    pre = dummy
    index = 0
    left = None
    left2 = None

    while cur is not None:
        index += 1
        # 到达m，记录当前的cur和pre，用于反转完成后拼接，left2.next 应该指向第n+1个节点，left应该指向第n个节点
        if index == m:
            left = pre
            left2 = cur

        # 范围内翻转
        if m < index < n:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            continue

        # 到达n，拼接，注意这时候cur指向第n个，需要调整cur.next
        if index == n:
            left2.next = cur.next
            cur.next = pre
            left.next = cur
            break

        pre = pre.next
        cur = cur.next

    return dummy.next


if __name__ == "__main__":
    header = gen_list('1->2->3->4->5')
    print_node(reverse(header, 2, 4))
