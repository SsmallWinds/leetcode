'''
题目描述
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和'*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。

说明:

s 可能为空，且只包含从a-z 的小写字母。

p 可能为空，且只包含从a-z 的小写字母，以及字符 .和 *。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

解析：
对于查找问题，需要划分子问题
输入: s[i...n]
表达式: p[j...m]

结果: f(s[i, n], p[j, m])

1.当s[i] == p[j] or p[j] == '.' 时, f(s[i, n], p[j, m]) = f(s[i + 1, n], p[j + 1, m])
2.当p[j + 1] == '*' and s[i] != p[j] and p[j] != '.'时，f(s[i, n], p[j, m]) = f(s[i, n], p[j + 2, m])
  即当前条件下，p的第一个 x* 对应匹配的字符个数是0，直接忽略掉即可
3.当p[j + 1] == '*' and (s[i] == p[j] or p[j] == '.')时，f(s[i, n], p[j, m]) = f(s[i + 1, n], p[j, m])
  即当前条件下，至少s[i] 这个字符是符合条件的，继续匹配下一个字符即可
'''

# 1.暴力法
def is_match(input:str, regx:str)->bool:
    if input == regx:
        return True
    first_match = len(input) != 0 and len(regx) != 0 and (input[0] == regx[0] or regx[0] == '.')
    if len(regx) >= 2 and regx[1] == '*': # 对应条件2,3 的前置条件
        return is_match(input, regx[2:]) or (first_match and is_match(input[1:], regx)) # 条件2 或 条件3
    return first_match and is_match(input[1:], regx[1:]) # 条件1

# 2.动态规划
def is_match2(input:str, regx:str)->bool:
    # dp[i][j] 表示 input[0...i] 和 regx[0...j] 的匹配情况
    dp=[[False for _ in range(len(regx) + 1)] for _ in range(len(input) + 1)]
    # 两个空字符串是匹配的
    dp[0][0] = True
    # x*y*z* 等可以匹配空字符串
    for i in range(1, len(regx)):
        dp[0][i] = dp[0][i - 2] if regx[i - 1] == '*' else False

    for i in range(1, len(input) + 1):
        for j in range(1, len(regx) + 1):
            # 条件1
            if input[i - 1] == regx[j - 1] or regx[j - 1] == '.':
                dp[i][j] = dp[i -1][j - 1]
            if regx[j - 1] == '*':
                # 对应条件2 x* 与 -----x* 等效
                dp[i][j] = dp[i][j - 2]
                # 对应条件3 input[.*] or input[x*] 与 regx[x] 等效于 input 与 regx[x*]|reg[.*] 匹配
                if input[i - 1] == regx[j - 2] or regx[j - 2] == '.':
                    dp[i][j] = dp[i - 1][j]
    return dp[len(input)][len(regx)]
    

if __name__ == "__main__":
    input='mississippi'
    regx='mis*is*ip*.'

    print(is_match(input, regx))
    print(is_match2(input, regx))