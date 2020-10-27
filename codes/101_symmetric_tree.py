"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

思路1:
遍历左子树A和右子树B
1.判断A和B根节点是否相等
2.递归判断A的左子树和B的右子树是否相等，且A的右子树和B的左子树是否相等

思路2:
前序遍历一般为中左右
这里改为左子树中左右, 右子树中右左, 判断序列是否相同
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


def is_symmetric(left: TreeNode, right: TreeNode) -> bool:
    if left is None and right is None:
        return True

    if left is None and right is not None:
        return False

    if left is not None and right is None:
        return False

    if not is_same(left, right):
        return False

    if not (is_symmetric(left.left, right.right) and
            is_symmetric(left.right, right.left)):
        return False

    return True


def is_symmetric2(left: TreeNode, right: TreeNode) -> bool:
    s_left = []
    s_right = []
    cur_left = left
    cur_right = right
    while len(s_left) > 0 or cur_left is not None or len(s_right) > 0 or cur_right is not None:
        while cur_left is not None:
            s_left.append(cur_left)
            cur_left = cur_left.left

        while cur_right is not None:
            s_right.append(cur_right)
            cur_right = cur_right.right

        if len(s_left) != len(s_right):
            return False

        temp_left = s_left.pop(0)
        temp_right = s_right.pop(0)
        if temp_left.val != temp_right.val:
            return False

        cur_left = temp_left.right
        cur_right = temp_right.left

    return True


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

    print(is_symmetric(root.left, root.right))
    print(is_symmetric2(root.left, root.right))
