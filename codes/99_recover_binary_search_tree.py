"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3


思路：
中序排列找到对应的两个节点，再交换
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root: TreeNode) -> None:
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


def recover1(root: TreeNode) -> None:
    s = []
    n1 = None
    n2 = None
    pre = None
    while root is not None or len(s) > 0:
        while root is not None:
            s.append(root)
            root = root.left
        cur = s.pop()
        # print(cur.val)
        if pre is not None and pre.val > cur.val:
            n2 = cur
            if n1 is None:
                n1 = pre
        pre = cur
        root = cur.right

    temp = n1.val
    n1.val = n2.val
    n2.val = temp


pre = None
n1 = None
n2 = None


def do_recover2(root: TreeNode) -> None:
    global pre, n1, n2
    if root is None:
        return

    do_recover2(root.left)
    print(pre, root.val)
    if pre is not None and pre.val > root.val:
        n2 = root
        if n1 is None:
            n1 = pre
    pre = root
    do_recover2(root.right)


def recover2(root: TreeNode) -> None:
    global n1, n2
    do_recover2(root)
    temp = n1.val
    n1.val = n2.val
    n2.val = temp


if __name__ == "__main__":
    root = TreeNode(10)
    a1 = TreeNode(12)
    a2 = TreeNode(15)
    b1 = TreeNode(5)
    b2 = TreeNode(20)

    root.left = a1
    root.right = a2

    a2.left = b1
    a2.right = b2

    # recover1(root)
    # print_tree(root)
    recover2(root)
    print_tree(root)
