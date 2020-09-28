"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

"""


def get_char(i: int):
    return chr(ord('A') + i - 1)


def do_decode(s: str, res: list, temp: list, index: int) -> str:
    from copy import copy
    if index == len(s):
        res.append(''.join([get_char(int(i)) for i in temp]))
        # res.append(copy(temp))
        return

    if index < len(s):
        temp.append(s[index])
        do_decode(s, res, temp, index + 1)
        temp.pop()
        if int(s[index: index + 2]) <= 26:
            temp.append(s[index: index + 2])
            do_decode(s, res, temp, index + 2)
            temp.pop()


# 递归，可用查找表优化
def do_decode2(s: str, index: int) -> int:
    if index == len(s):
        return 1

    if s[index] == '0':
        return 0

    res1 = do_decode2(s, index + 1)
    res2 = 0
    if index < len(s) - 1:
        if s[index] != '0' and int(s[index: index + 2]) <= 26:
            res2 = do_decode2(s, index + 2)
    return res1 + res2


# 能递归一般可以动态规划
# dp[n] = dp[n + 1] + dp[n + 2]
# 主要麻烦的是0的情况的处理 考虑输入'101', '01', '00', '10', '230'等
def decode3(s: str) -> int:
    if len(s) == 0:
        return 0
    if s[0] == '0':
        return 0
    dp = [0 for _ in range(len(s))]
    if s[0] != '0':
        dp[0] = 1
    if len(s) == 1:
        return dp[0]

    dp[1] = 1 if s[0] > '0' and s[1] > '0' else 0
    if 1 <= int(s[:2]) <= 26:
        dp[1] += 1

    for i in range(2, len(s)):
        if s[i] != '0':
            dp[i] = dp[i - 1]
        if s[i - 1] != '0' and int(s[i - 1: i + 1]) <= 26:
            dp[i] += dp[i - 2]

    return dp[len(s) - 1]


# 优化空间复杂度
# 当前值只依赖前两个值，可将空间复杂度优化为O(1)
def decode4(s: str) -> int:
    if len(s) == 0:
        return 0
    if s[0] == '0':
        return 0
    one = 0
    two = 0
    if s[0] != '0':
        one = 1
    if len(s) == 1:
        return one

    two = 1 if s[0] > '0' and s[1] > '0' else 0
    if 1 <= int(s[:2]) <= 26:
        two += 1

    for i in range(2, len(s)):
        cur = 0
        if s[i] != '0':
            cur = two
        if s[i - 1] != '0' and int(s[i - 1: i + 1]) <= 26:
            cur += one
        one = two
        two = cur
    return two


if __name__ == "__main__":
    s = '230'
    res = []
    # do_decode(s, res, [], 0)
    # print(do_decode2(s, 0))
    print(decode3(s))
    print(decode4(s))
    # print(res)
