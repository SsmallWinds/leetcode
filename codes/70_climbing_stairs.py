"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

得出子问题:
上到第n个台阶可以是以下可能
a> 先到第n-1再走1步
b> 先到第n-2再走2步
c> 先到第n-2再走两个1步
其中a和c实质上是一种走法
令结果为f(n)，得到：
f(1) = 1
f(2) = 2
f(n) = f(n - 1) + f(n - 2)

非常经典的问题，思路上从递归->递归查找表优化->动态规划->动态规划的时间复杂度优化

另外还有题目的非通用解法: 矩阵相乘， 公式法见https://leetcode.wang/leetCode-70-Climbing-Stairs.html
"""

# 递归
def climbing(n:int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return climbing(n - 1) + climbing(n - 2)

# 递归优化，将已经算过的值保存起来,防止重复计算
def climbing2(n:int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    temp = {}
    r1 = temp.get(n - 1, None)
    if r1 is None:
        r1 = climbing2(n - 1)
        temp[n - 1] = r1
    r2 = temp.get(n - 2, None)
    if r2 is None:
        r2 = climbing2(n - 2)
        temp[n - 2] = r2
    return r1 + r2

# 动态规划
def climbing3(n:int) -> int:
    dp = [0 for _ in range(n)]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[-1]

# 动态规划, 优化空间，子问题只有n -1 和 n -2, 空间复杂度可以为O(1)
def climbing4(n:int) -> int:
    n1 = 1
    n2 = 2

    if n == 1:
        return n1
    
    if n == 2:
        return n2

    # 向后移动一位
    for i in range(2, n):
        temp = n2
        n2 = n1 + n2
        n1 = temp

    return n2

if __name__ == '__main__':
    print(climbing(3))
    print(climbing2(3))
    print(climbing3(3))
    print(climbing4(3))
    