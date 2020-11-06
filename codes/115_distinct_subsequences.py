"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^

思路:
s和t的子串记为s[0,len], t[0,len], 结果记为n
当s[0] == t[0]时:
    当s选s[0]且t选t[0]时，结果n1为s[1,len] t[1,len]的结果
    当s不选s[0]时，t选t[0]时，结果n2为s[1, len] t[0, len]的结果
当s[0] != t[0] 时:
    s一定不能选s[0]，t选t[0], 结果为 n1

子问题的分解思路如上
递归的出口为t为空串时，s中不能选一个字母一种可能，即选法为1
s为空串时，从空串中无法选择，即选法为0

递归可用字典优化重复计算
且一般可用动态规划优化

动态规划递推公式
dp[m][n] 对应 s[m,len]和t[n,len]的结果
有dp[m,n]
if m == len:(即s为空串)
    dp[m][n] = 0
if n == len:(即t为空串)
    dp[m][n] = 1
if s[m] == t[n]:
    dp[m][n] = dp[m + 1][n + 1] + dp[m + 1][n]
else:
    dp[m][n] = dp[m + 1][n]
"""


def distinct_subsequences(s: str, s_start: int, t: str, t_start: int) -> int:
    if t_start == len(t):
        return 1

    if s_start == len(s):
        return 0

    res = 0
    if s[s_start] == t[t_start]:
        res = distinct_subsequences(s, s_start + 1, t, t_start + 1) + distinct_subsequences(s, s_start + 1, t, t_start)
    else:
        res = distinct_subsequences(s, s_start + 1, t, t_start)

    return res


def distinct_subsequences2(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for index in range(len(s) + 1):
        dp[index][len(t)] = 1
    for m in range(len(s) - 1, -1, -1):
        for n in range(len(t) - 1, -1, - 1):
            if s[m] == t[n]:
                dp[m][n] = dp[m + 1][n + 1] + dp[m + 1][n]
            else:
                dp[m][n] = dp[m + 1][n]

    return dp[0][0]


if __name__ == "__main__":
    s = 'babgbag'
    t = 'bag'
    print(distinct_subsequences(s, 0, t, 0))
    print(distinct_subsequences2(s, t))
