"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

回溯法
"""


def is_swap(sz: list, start: int, end: int) -> bool:
    for i in range(start, end):
        if sz[i] == sz[end]:
            return False
    return True


def swap(raw: list, start: int, end: int):
    temp = raw[start]
    raw[start] = raw[end]
    raw[end] = temp


def do_permutations(raw: list, res: list, start: int, end: int):
    import copy
    if start == end:
        res.append(copy.copy(raw))
        return

    for i in range(start, end):
        # if is_swap(raw, start, i):
        swap(raw, start, i)
        do_permutations(raw, res, start + 1, end)
        swap(raw, start, i)


def permutations(raw: list):
    res = []
    do_permutations(raw, res, 0, len(raw))
    return res


if __name__ == "__main__":
    print(permutations([1, 2, 3]))
