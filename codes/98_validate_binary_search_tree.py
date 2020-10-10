"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

思路:
二叉搜索树的定义是，树的每个节点的左子树中节点一定小于当前节点且右子树中节点一定大于当前节点


思路1:
通过每个值的取值范围是否合法判断

思路2:
中序遍历二叉搜索树应该是一个有序的序列

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def check(root:TreeNode) -> bool:
    # 遍历过程是先序遍历即DFS
    def _do_check(root:TreeNode, min_val:int, max_val:int) -> bool:
        if root is None:
            return True
        
        if min_val is not None and root.val <= min_val:
            return False

        if max_val is not None and root.val >= max_val:
            return False
        
        return _do_check(root.left, min_val, root.val) and _do_check(root.right, root.val, max_val)

    return _do_check(root, None, None)

def check2(root:TreeNode) -> bool:
    # BFS
    def _do_check(root:TreeNode) -> bool:
        q = []
        q.append((root, None, None))
        while len(q) > 0:
            cur = q.pop(0)
            cur_val = cur[0].val
            min_val = cur[1]
            max_val = cur[2]

            if min_val is not None and cur_val <= min_val:
                return False
            if max_val is not None and cur_val >= max_val:
                return False

            if cur[0].left is not None:
                q.append((cur[0].left, cur[1], cur[0].val))
            if cur[0].right is not None:
                q.append((cur[0].right, cur[0].val, cur[2]))
        return True

    return _do_check(root)

def check3(root:TreeNode, pre:int) -> bool:
    # 中序遍历
    if root is None:
        return True

    pre = None
    s = []
    while len(s) > 0 or root is not None:
        while root is not None:
            s.append(root)
            root = root.left
        cur = s.pop()
        if pre is not None and pre >= cur.val:
            return False
        pre = cur.val
        root = cur.right

    return True

if __name__ == "__main__":
    root = TreeNode(10)
    a1 = TreeNode(5)
    a2 = TreeNode(15)
    b1 = TreeNode(12)
    b2 = TreeNode(20)

    root.left = a1
    root.right = a2

    a2.left = b1
    a2.right = b2

    print(check(root))
    print(check2(root))
    print(check3(root, None))