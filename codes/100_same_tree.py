"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

思路:
同时以相同方式遍历比较每个节点是否相同即可
需要注意节点为空的情况
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same(node1: TreeNode, node2: TreeNode) -> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is not None and node2 is not None:
        if node1.val == node2.val:
            return True

    return False


def check(node1: TreeNode, node2: TreeNode) -> bool:
    if node1 is None and node2 is None:
        return True

    if node1 is None and node2 is not None:
        return False

    if node1 is not None and node2 is None:
        return False

    if not check(node1.left, node2.left):
        return False

    if not is_same(node1, node2):
        return False

    if not check(node1.right, node2.right):
        return False

    return True


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

    root1 = TreeNode(10)
    a11 = TreeNode(12)
    a12 = TreeNode(15)
    b11 = TreeNode(5)
    b12 = TreeNode(20)

    root1.left = a11
    root1.right = a12

    a12.left = b11
    a12.right = b12

    print(check(root, root1))
