"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

思路：
前序遍历的顺序是 当前节点->左子树->右子树
中序遍历的顺序是 左子树->当前节点->右子树

所以前序遍历的顺序很容易能得到树的根节点
通过中序遍历的结果可以得到左子树的中序序列和右子树的中序序列

根据得到的左子树序列长度能得和前序遍历的结果能得到左子树前序遍历的结果
通过子树的前序遍历和中序遍历，递归即可构恢复原始的树
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


def pre_order_print(root: TreeNode) -> None:
    if root is None:
        return

    print(root.val)
    pre_order_print(root.left)
    pre_order_print(root.right)


# TODO:: 优化，不需要每次列表分片，可用两个index标记子序列的范围，这时找根节点的index自然可用map优化
def do_build_tree(pre_order: list, in_order: list):
    if len(pre_order) <= 0:
        return None

    root_index = 0
    root_node = TreeNode(pre_order[0])
    for index in range(len(in_order)):
        if in_order[index] == root_node.val:
            root_index = index
            break
    left_pre_order = pre_order[1:root_index + 1]
    left_in_order = in_order[:root_index]

    right_pre_node = pre_order[root_index + 1:]
    right_in_node = in_order[root_index + 1:]

    root_node.left = do_build_tree(left_pre_order, left_in_order)
    root_node.right = do_build_tree(right_pre_node, right_in_node)
    return root_node


def build_tree(pre_order: list, in_order: list) -> TreeNode:
    tree = do_build_tree(pre_order, in_order)
    pre_order_print(tree)
    print('--')
    in_order_print(tree)


if __name__ == "__main__":
    pre_order = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 7]
    in_order = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]
    build_tree(pre_order, in_order)
