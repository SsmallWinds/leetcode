"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order_print(root: TreeNode) -> None:
    if root is None:
        return

    in_order_print(root.left)
    print(root.val)
    in_order_print(root.right)


def build_tree(nums: list) -> TreeNode:
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return TreeNode(nums[0])

    index = int(len(nums) / 2)
    res = TreeNode(nums[index])
    res.left = build_tree(nums[:index])
    res.right = build_tree(nums[index + 1:])
    return res


if __name__ == "__main__":
    t = build_tree([1, 2, 3, 4, 5, 6])
    in_order_print(t)
