"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

思路基本和105一致，后续的最后一个节点是根节点，可区分左右子树
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


def post_order_print(root: TreeNode) -> None:
    if root is None:
        return

    post_order_print(root.left)
    post_order_print(root.right)
    print(root.val)


# TODO:: 优化，不需要每次列表分片，可用两个index标记子序列的范围，这时找根节点的index自然可用map优化
def do_build_tree(post_order: list, in_order: list):
    if len(post_order) <= 0:
        return None

    root_index = 0
    root_node = TreeNode(post_order[-1])
    for index in range(len(in_order)):
        if in_order[index] == root_node.val:
            root_index = index
            break
    left_in_order = in_order[:root_index]
    left_post_order = post_order[:root_index]

    right_in_node = in_order[root_index + 1:]
    right_post_order = post_order[root_index: len(post_order) - 1]

    root_node.left = do_build_tree(left_post_order, left_in_order)
    root_node.right = do_build_tree(right_post_order, right_in_node)
    return root_node


def build_tree(post_order: list, in_order: list) -> TreeNode:
    tree = do_build_tree(post_order, in_order)
    in_order_print(tree)
    print('--')
    post_order_print(tree)


if __name__ == "__main__":
    in_order = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]
    post_order = [8, 9, 4, 10, 11, 5, 2, 6, 7, 3, 1]
    build_tree(post_order, in_order)
