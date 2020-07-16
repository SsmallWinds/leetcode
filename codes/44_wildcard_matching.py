"""
说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

输入: s[i...n]
表达式: p[j...m]
和10题类似，区别是11题*需要考虑*前的元素，本题不用

当 p[j] == '*'时 dp[i][j] = dp[i][j - 1] or (i > 0 and dp[i - 1][j])
否则判断 p[j] 是否等于 s[i] 或者 ? ,符合则有 dp[i][j] = dp[i - 1][j - 1]
"""


# 动态规划
def is_match2(input: str, regx: str) -> bool:
    # dp[i][j] 表示 input[0...i] 和 regx[0...j] 的匹配情况
    dp = [[False for _ in range(len(regx) + 1)] for _ in range(len(input) + 1)]
    # 两个空字符串是匹配的
    dp[0][0] = True

    for i in range(0, len(input) + 1):
        for j in range(1, len(regx) + 1):
            if regx[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or (i > 0 and dp[i - 1][j])
            else:
                if i > 0 and (input[i - 1] == regx[j - 1] or regx[j - 1] == '?'):
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[len(input)][len(regx)]


if __name__ == "__main__":
    input = 'acdcb'
    regx = '*cd*'

    print(is_match2(input, regx))
