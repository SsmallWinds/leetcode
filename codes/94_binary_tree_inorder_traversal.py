"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
def inorder_traversal(head:TreeNode, res:list) -> None:
    
    if head.left is not None:
        inorder_traversal(head.left, res)

    res.append(head.val)

    if head.right is not None:
        inorder_traversal(head.right, res)


# 迭代
def inorder_traversal2(head:TreeNode) -> list:
    res = []
    temp = []
    cur = head

    while cur is not None or len(temp) > 0:
        while cur is not None:
            temp.append(cur)
            cur = cur.left
        
        cur = temp.pop()
        res.append(cur.val)
        cur = cur.right

    print(res)



if __name__ == "__main__":
    head = TreeNode(val=0)
    left1 = TreeNode(val=1)
    right1 = TreeNode(val=2)
    head.left = left1
    head.right = right1

    left2 = TreeNode(val=3)
    right2 = TreeNode(val=4)
    left1.left = left2
    left1.right = right2

    left3 = TreeNode(val=5)
    right3 = TreeNode(val=6)
    left2.left = left3
    left2.right = right3

    res = []
    inorder_traversal(head, res)
    inorder_traversal2(head)
    print(res)