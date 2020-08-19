"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

算字符串距离,经典动态规划问题
子问题分析：
令结果集dp = [][]
dp[x][y] 为 子串 A[0 ~ n] 到 子串B[0 ~ n] 的距离

dp[0][y] = y 从空字符串到任意字符串都只能添加
dp[x][0] = x 从任意字符串到空字符串都是只能删除

剩下的情况dp[x][y] 等于以下几种情况的最小值
1> A[x - 1] == b[y - 1] 时dp[x][y] = dp[x -1][y - 1] 即最后一个字符不需要变化
2> A[x - 1] != b[y - 1] 时dp[x][y] = dp[x -1][y - 1] + 1 即最后一个字符替换
3> dp[x - 1][y] + 1 即需要增加一个字符
4> dp[x][y - 1] 即需要减去一个字符

"""

def distance(a:str, b:str) -> int:
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(b) + 1):
        dp[0][i] = i

    for i in range(len(a) + 1):
        dp[i][0] = i

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            a1 = dp[i - 1][j - 1]
            a2 = dp[i - 1][j] + 1
            a3 = dp[i][j - 1] + 1
            if a[i - 1] != b[j - 1]:
                a1 += 1
            dp[i][j] = min(a1, a2, a3)

    return dp[-1][-1]


if __name__ == "__main__":
    print(distance('horse','ros'))