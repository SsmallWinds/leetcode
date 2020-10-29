"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5


 思路1. 将链表转为数组，套用108的方法
 思路2. 套用108的方法，使用快慢指针获取中间值
 思路3. 利用中序遍历的顺序，给树赋值
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


cur = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
cur.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


def in_order_print(root: TreeNode) -> None:
    if root is None:
        return

    in_order_print(root.left)
    print(root.val)
    in_order_print(root.right)


def build_tree(head: int, end: int) -> TreeNode:
    global cur
    if head == end:
        return None

    mid = int((head + end) / 2)
    left = build_tree(head, mid)
    root = TreeNode(cur.val)
    root.left = left
    cur = cur.next
    # print('mid:', mid, cur.val)

    right = build_tree(mid + 1, end)
    root.right = right
    return root


if __name__ == "__main__":
    t = build_tree(0, 7)
    in_order_print(t)
