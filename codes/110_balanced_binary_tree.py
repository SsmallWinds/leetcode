"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def depth(root: TreeNode) -> int:
    if root is None:
        return 0

    return max(depth(root.left), depth(root.right)) + 1


def is_balance(root: TreeNode) -> bool:
    if root is None:
        return True
    if abs(depth(root.left) - depth(root.right)) > 1:
        return False
    return is_balance(root.left) and is_balance(root.right)


# 优化，在计算深度时就可以判断是否平衡了
def is_balance2(root: TreeNode) -> bool:
    if root is None:
        return 0

    left = is_balance2(root.left)
    right = is_balance2(root.right)

    if left == -1 or right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1


if __name__ == "__main__":
    root = TreeNode(3)
    a1 = TreeNode(1)
    a2 = TreeNode(15)
    b1 = TreeNode(10)
    b2 = TreeNode(20)
    c1 = TreeNode(22)

    root.left = a1
    root.right = a2

    a2.left = b1
    a2.right = b2

    # b2.right = c1

    print(is_balance(root))
    print(is_balance2(root) != -1)
