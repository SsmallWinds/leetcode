"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"

思路：
可将全排列分为 [0 ... n -1] 开头的n组，全排列数量为count = n!，第k个一定在 count / k 组中
即可确定第一位
剩下的移除确定的元素，剩下的重复即可
"""

def permutation2(n:int, k:int) -> list:
    import math
    res = []
    l = [i + 1 for i in range(n)]
    k -= 1
    for i in range(n):
        if len(l) == 1:
            res.append(l[0])
            break
        count = math.factorial(n - i - 1) # 每组的数量
        group = int(k / count) # 第几组
        res.append(l[group])
        del l[group]
        k %= count
    return res


if __name__ == "__main__":
    print(permutation2(4, 19))
