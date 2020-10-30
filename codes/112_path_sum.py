"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_leaf(root: TreeNode) -> bool:
    return root.left is None and root.right is None


# 本质是DFS
def do_check_sum(root: TreeNode, sum: int) -> bool:
    if is_leaf(root):
        return root.val == sum
    if root.left is None:
        return do_check_sum(root.right, sum - root.val)
    if root.right is None:
        return do_check_sum(root.left, sum - root.val)
    return do_check_sum(root.left, sum - root.val) or do_check_sum(root.right, sum - root.val)


def check_sum(root: TreeNode, sum: int) -> bool:
    if root is None:
        return False

    return do_check_sum(root, sum)


# BFS
def check_sum2(root: TreeNode, sum: int) -> bool:
    if root is None:
        return False

    q = [root]
    sums = [root.val]

    while len(q) > 0:
        size = len(q)
        for _ in range(size):
            cur = q.pop(0)
            cur_sum = sums.pop(0)
            if is_leaf(cur) and cur_sum == sum:
                return True

            if cur.left is not None:
                q.append(cur.left)
                sums.append(cur_sum + cur.left.val)

            if cur.right is not None:
                q.append(cur.right)
                sums.append(cur_sum + cur.right.val)
    return False


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
    print(check_sum2(root, 19))
