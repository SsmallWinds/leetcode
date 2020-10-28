"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

思路基本同102题普通的分层遍历
区别就是区奇偶的层的数组分别是插入到尾部和头部
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
    level = 0

    while len(q) > 0:
        num = len(q)
        temp = []
        for i in range(num):
            cur = q.pop(0)
            if level % 2 == 0:
                temp.append(cur.val)
            else:
                temp.insert(0, cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        res.append(temp)
        level += 1

    return res


def level_traversal2(root: TreeNode, level: int, res: list) -> list:
    if root is None:
        return

    if len(res) <= level:
        res.append([])

    if level % 2 == 0:
        res[level].append(root.val)
    else:
        res[level].insert(0, root.val)
    level_traversal2(root.left, level + 1, res)
    level_traversal2(root.right, level + 1, res)


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

    print(level_traversal(root))

    res = []
    level_traversal2(root, 0, res)
    print(res)
