"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

思路:
和62题类似，62题只需要判断边界，这题需要判断障碍物

动态规划的递推公式为:
if grid[n][m] == 1:
    dp(n,m) = 0 
else:
    dp(n+1,m) + dp(n,m+1)

"""

def path_count2(grid:list) -> int:
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    down = False
    for i in range(n - 1, -1, -1):
        if down:
            continue
        else:
            if grid[i][m - 1] == 1:
                down = True
            else:
                dp[i][m - 1] = 1
    
    down = False
    for j in range(m - 1, -1, -1):
        if down:
            continue
        else:
            if grid[n - 1][j] == 1:
                down = True
            else:
                dp[n -1][j] = 1

    for line in dp:
        print(line)

    for k in range(n - 2,-1,-1):
        for l in range(m - 2,-1,-1):
            if grid[k][l] == 1:
                dp[k][l] = 0
            else:
                dp[k][l] = dp[k + 1][l] + dp[k][l + 1]

    return dp[0][0]

if __name__ == "__main__":
    grid = [[0,0,0],\
            [0,1,0],\
            [0,0,0]]

    print(path_count2(grid))