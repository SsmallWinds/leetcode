"""
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false
"""


"""
递归判断是否符合
判断时检查字符串相等则一定符合，字符出现次数不一致则一定不符合
递归判断以每个字符作为分割的子串
假设字符串长度为6，i = 2时
情况1：子串没旋转时，则为判断a[0:1] b[0:1] 以及a[2:5] b[2:5]
情况2：旋转时，则为a[0:3] b[2:5] 以及a[4:5] b[0:1]

可用查找表优化，调用时现在判断是否已经判断过了比如 a#b 作为key
如果已经判断过则直接返回结果
"""
def is_scramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    counts1 = [0 for _ in range(27)]
    counts2 = [0 for _ in range(27)]
    for i in s1:
        counts1[ord(i) - ord('a')] += 1
    for i in s2:
        counts2[ord(i) - ord('a')] += 1
    for i in range(27):
        if counts1[i] != counts2[i]:
            return False
    for i in range(1, len(s1)):
        if is_scramble(s1[:i], s2[:i]) and is_scramble(s1[i:], s2[i:]):
            return True
        if is_scramble(s1[i:], s2[:len(s2) - i]) and is_scramble(s1[:i], s2[len(s2) - i:]):
            return True
    return False


"""
可以递归就要想到动态规划
本题多了一个维度
dp[len][i][j] 表示 s1[i,i+len] 和 s2[j,j+len]两个字符串是否满足条件,即从i开始的len个字符是否能转换为从j开始的len个字符
假设在位置q处切分
对应情况1 dp[len][i][j] = dp[q][i][j] && dp[len-q][i+q][j+q]
对应情况2 dp[len][i][j] = dp[len-q][i+q][j] && dp[q][i][j+len-q]
"""
def is_scramble2(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    counts1 = [0 for _ in range(27)]
    counts2 = [0 for _ in range(27)]
    for i in s1:
        counts1[ord(i) - ord('a')] += 1
    for i in s2:
        counts2[ord(i) - ord('a')] += 1
    for i in range(27):
        if counts1[i] != counts2[i]:
            return False

    dp = [[[False for _ in range(len(s1) + 1)]for _ in range(len(s1) + 1)] for _ in range(len(s1) + 1)]
    for length in range(1, len(s1) + 1):
        for i in range(len(s1) - length + 1):
            for j in range(len(s2) - length + 1):
                if length == 1:
                    dp[length][i][j] = s1[i] == s2[j]
                else:
                    for q in range(1, length):
                        dp[length][i][j] = (dp[q][i][j] and dp[length-q][i+q][j+q]) or\
                                           (dp[length-q][i+q][j] and dp[q][i][j+length-q])
                        if dp[length][i][j]:
                            break

    return dp[len(s1)][0][0]


# MARK WEAK
if __name__ == "__main__":
    s1 = 'rgeat'
    s2 = 'eatrg'
    print(is_scramble(s1, s2))
    print(is_scramble2(s1, s2))
