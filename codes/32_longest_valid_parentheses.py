"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

思路：
暴力法
遍历输入，找到每个位置的最大值

动态规划
dp[i] 为以raw[i]结尾的匹配的字符串长度
’(‘ 结尾一定为非法
’)‘ 结尾：
    如果上一个是’(’ 则直接 xxxx() dp[i] = dp[i - 2] + 2
    如果上一个是‘)’ 如 xxxx)) 则看dp[i - 1] 对应子串的左边一个是不是 ‘(’ 如 (()) 或者 ()()(())
    如果是 则 dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + dp[i - 2]
    加上dp[i - dp[i - 1] - 2] 是因为dp[i - 1] 左边符号的前面可能也有符合的子串
"""


def check(raw: str, start: int, end: int) -> None:
    if start == end:
        return False

    balance = 0
    for i in range(start, end + 1):
        if raw[i] == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                return False
    return balance == 0


# 暴力法，时间复杂度为O(n ^ 3)
def calc(raw: str) -> int:
    max_val = -1
    for i in range(len(raw)):
        for j in range(i + 1, len(raw)):
            if check(raw, i, j) and (max_val < j - i + 1):
                max_val = j - i + 1

    return max_val


# 动态规划只遍历一次 时间复杂度为 O(n)
def calc2(raw: str) -> int:
    dp = [0 for _ in raw]
    for i in range(1, len(raw)):
        if raw[i] == '(':
            continue
        else:
            if raw[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            else:
                if i - dp[i - 1] > 0 and raw[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0) + 2
    return max(dp)


if __name__ == "__main__":
    print(calc(')()())'))
    print(calc2(')()())'))
    print(calc2('()()(())'))
    print(calc2('())'))
