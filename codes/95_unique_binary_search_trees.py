"""
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(root:TreeNode):
    res = []
    temp = []
    temp.append(root)

    while len(temp) > 0:
        cur = temp.pop(0)
        if cur is None:
            res.append(None)
        else:
            res.append(cur.val)
            temp.append(cur.left)
            temp.append(cur.right)
    while len(res) > 0 and res[len(res) - 1] is None:
        res.pop()
    print(res)

def do_gen_tree(start:int, end:int) -> list:
    res = []
    if start > end:
        res.append(None)
        return res

    # 只有一个数, 直接塞自己返回
    if start == end:
        node = TreeNode(val = start)
        res.append(node)
        return res

    for i in range(start, end + 1):
        left_tree = do_gen_tree(start, i - 1)
        right_tree = do_gen_tree(i + 1, end)
        for left in left_tree:
            for right in right_tree:
                node = TreeNode(val=i)
                node.left = left
                node.right = right
                res.append(node)

    return res


if __name__ == "__main__":
    res = do_gen_tree(1, 4)
    for node in res:
        printTree(node)

