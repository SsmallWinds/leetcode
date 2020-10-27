"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_traversal(root: TreeNode) -> list:
    if root is None:
        return
    q = [root]
    res = []

    while len(q) > 0:
        num = len(q)
        temp = []
        for i in range(num):
            cur = q.pop(0)
            temp.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        res.append(temp)

    return res


def level_traversal2(root: TreeNode, level: int, res: list) -> list:
    if root is None:
        return

    if len(res) <= level:
        res.append([])

    res[level].append(root.val)
    level_traversal2(root.left, level + 1, res)
    level_traversal2(root.right, level + 1, res)


if __name__ == "__main__":
    root = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(2)
    b1 = TreeNode(3)
    b2 = TreeNode(4)
    b3 = TreeNode(4)
    b4 = TreeNode(3)

    root.left = a1
    root.right = a2

    a1.left = b1
    a1.right = b2
    a2.left = b3
    a2.right = b4

    print(level_traversal(root))

    res = []
    level_traversal2(root, 0, res)
    print(res)
