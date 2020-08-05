"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

思路：
拿到题目应该能想到可以将问题转换为子问题处理
然后对应的就是递归和动态规划的思路

子问题：
(0,0) -> (n-1, m-1)  = (0,1)->(n-1, m-1) + (1,0)->(n-1, m-1)
"""

def calc(x:int, y:int, n:int, m:int) -> int:
    if x == n and y == m:
        return 1
    
    n1 = 0
    n2 = 0

    if x + 1 <= n:
        n1 = calc(x + 1, y, n, m)
    
    if y + 1 <= m:
        n2 = calc(x, y + 1, n, m)
    return n1 + n2

# 递归方法
def path_count1(n:int, m:int) -> int:
    return calc(0, 0, n - 1, m - 1)

# 动态规划 dp(n,m) = dp(n+1,m) + dp(n,m+1)
def path_count2(n:int, m:int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # 最后一行和最后一列只能往右走和往下走，所以值为1
    for i in range(n):
        dp[i][m - 1] = 1
    
    for j in range(m):
        dp[n - 1][j] = 1

    for k in range(n - 2,-1,-1):
        for l in range(m - 2,-1,-1):
            dp[k][l] = dp[k + 1][l] + dp[k][l + 1]

    return dp[0][0]

# TODO:: 优化空间复杂度 https://blog.csdn.net/qq_31362767/article/details/81702491

if __name__ == "__main__":
    print(path_count1(3, 7))
    print(path_count2(3, 7))