"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

沿着62题思路
 dp(n,m) = grid(n, m) + min(dp(n+1,m), dp(n,m+1))
 可以递归，动态规划
"""

# 递归
def calc(x:int, y:int, grid:list) -> int:
    import sys
    n = len(grid) - 1
    m = len(grid[0]) - 1
    if x == n and y == m:
        return grid[x][y]
    
    n1 = sys.maxsize
    n2 = sys.maxsize

    if x + 1 <= n:
        n1 = calc(x + 1, y, grid)
    
    if y + 1 <= m:
        n2 = calc(x, y + 1, grid)
    return grid[x][y] + min(n1, n2)

def path_min(grid:list):
    return calc(0, 0, grid)

"""
TODO:: 可优化，计算过的节点可以用hash表记录下来，
获取子问题解时，先判断是否计算过，没计算过再递归计算
"""

# 动态规划
def path_min2(grid:list) -> int:
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    dp[n - 1][m - 1] = grid[n - 1][m - 1]

    # 最后一行和最后一列只能往右走和往下走，所以值为1
    for i in range(n - 2, -1, -1):
        dp[i][m - 1] = grid[i][m - 1] + dp[i + 1][m - 1]
    
    for j in range(m - 2, -1, -1):
        dp[n - 1][j] = grid[n - 1][j] + dp[n - 1][j + 1]

    for k in range(n - 2,-1,-1):
        for l in range(m - 2,-1,-1):
            dp[k][l] = grid[k][l] + min(dp[k + 1][l], dp[k][l + 1])

    return dp[0][0]


if __name__ == "__main__":
    grid = [[1,3,1],\
            [1,5,1],\
            [4,2,1]]

    print(path_min(grid))
    print(path_min2(grid))