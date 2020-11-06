"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_leaf(root: TreeNode) -> bool:
    return root.left is None and root.right is None


# 本质是DFS,用一个数组记录路径,递归完(相当于出栈时)需要pop()
def do_check_sum(root: TreeNode, sum: int, res: list, temp: list) -> None:
    if is_leaf(root):
        if root.val == sum:
            temp.append(root.val)
            res.append(copy.copy(temp))
            temp.pop()
        return

    if root.left is None:
        temp.append(root.val)
        do_check_sum(root.right, sum - root.val, res, temp)
        temp.pop()
        return
    if root.right is None:
        temp.append(root.val)
        do_check_sum(root.left, sum - root.val, res, temp)
        temp.pop()
        return

    temp.append(root.val)
    do_check_sum(root.left, sum - root.val, res, temp)
    temp.pop()

    temp.append(root.val)
    do_check_sum(root.right, sum - root.val, res, temp)
    temp.pop()


def check_sum(root: TreeNode, sum: int) -> list:
    if root is None:
        return False

    res = []
    do_check_sum(root, sum, res, [])
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(3)
    b1 = TreeNode(4)
    b2 = TreeNode(5)
    b3 = TreeNode(6)
    b4 = TreeNode(7)
    c1 = TreeNode(8)
    c2 = TreeNode(9)
    c3 = TreeNode(10)
    c4 = TreeNode(11)

    root.left = a1
    root.right = a2

    a1.left = b1
    a1.right = b2
    a2.left = b3
    a2.right = b4

    b1.left = c1
    b1.right = c2
    b2.left = c3
    b2.right = c4

    print(check_sum(root, 19))
