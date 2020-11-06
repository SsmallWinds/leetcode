"""
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flatten(root: TreeNode) -> TreeNode:
    while root is not None:
        # 左节点为空直接考虑下个节点
        if root.left is None:
            root = root.right
        else:
            # 找到左子树的最右边节点
            pre = root.left
            while pre.right is not None:
                pre = pre.right

            # 将右子树接到左子树的最右边节点
            pre.right = root.right
            # 将左子树接到root的右节点
            root.right = root.left
            # root的左节点置为空
            root.left = None
            # 移动root节点为右子树的根节点
            root = root.right
