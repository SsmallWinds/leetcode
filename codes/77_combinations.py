"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

思路：
选数字类型的题目，回溯法，思路同全排列类似 No 46

TODO:: 其他解法 https://leetcode.wang/leetCode-77-Combinations.html

"""

def do_combinations(res:list, k:int, start:int, n:int, temp:list) -> None:
    import copy
    if len(temp) == k:
        res.append(copy.copy(temp))
        return

    for i in range(start, n + 1):
        temp.append(i)
        do_combinations(res, k, i + 1, n, temp)
        temp.pop()

def combinations(n:int, k:int) -> list:
    res = []
    do_combinations(res, k, 1, n, [])
    return res

if __name__ == "__main__":
    print(combinations(4, 3))
