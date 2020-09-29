"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


思路和95一致，不需要保存结果了
很经典的递归到记录优化到动态规划

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

def do_gen_tree(start:int, end:int) -> int:
   res = 0
   if start > end:
      return 1

   # 只有一个数, 直接塞自己返回
   if start == end:
      return 1

   for i in range(start, end + 1):
      left = do_gen_tree(start, i - 1)
      right = do_gen_tree(i + 1, end)
      res += left * right

   return res

# 由于只需要数量。不需要范围，只需要数量
# 可以用hash表记录已经算过的数量
def do_gen_tree2(count:int) -> int:
   if count <=1:
      return 1

   res = 0
   for i in range(1, count + 1):
      left = do_gen_tree2(i - 1)
      right = do_gen_tree2(count - i)
      res += left * right

   return res


# 可以递归一般可以动态规划
# dp[i] 表示 长度为i的数组有多少可能的子树
def do_gen_tree3(count:int) -> int:
   dp = [0 for _ in range(count + 1)]
   dp[0] = 1

   for i in range(1, count + 1): # 数量
      for j in range(1, i + 1): # 分割的节点
         dp[i] += dp[j - 1] * dp[i - j]

   return dp[-1]

if __name__ == "__main__":
   print(do_gen_tree(1, 3))
   print(do_gen_tree2(3))
   print(do_gen_tree3(3))

