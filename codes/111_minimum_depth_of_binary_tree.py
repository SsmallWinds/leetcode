"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_leaf(root: TreeNode) -> bool:
    return root.left is None and root.right is None


def minimum_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    q = [root]
    depth = 1

    while len(q) > 0:
        size = len(q)
        for i in range(size):
            cur = q.pop(0)
            # print(cur.val)
            if is_leaf(cur):
                return depth
            if cur.left is not None:
                q.append(cur.left)

            if cur.right is not None:
                q.append(cur.right)

        depth += 1
    return depth


def minimum_depth2(root: TreeNode) -> int:
    if root is None:
        return 0

    if root.left is None:
        return minimum_depth2(root.right) + 1

    if root.right is None:
        return minimum_depth2(root.left)

    return min(minimum_depth2(root.left), minimum_depth2(root.right)) + 1


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

    print(minimum_depth(root))
    print(minimum_depth2(root))
