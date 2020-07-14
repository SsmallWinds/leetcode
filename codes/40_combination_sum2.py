"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


# 回溯法, 思路同39题，只是改为了不能重复利用
def back_trace(res: list, temp: list, raw: list, remain: int, start: int) -> None:
    import copy
    if remain < 0:
        return
    elif remain == 0:
        # 去重
        if temp not in res:
            res.append(copy.copy(temp))
        return
    else:
        for i in range(start, len(raw)):
            temp.append(raw[i])
            # 不能重复使用，则传入i + 1 即可
            back_trace(res, temp, raw, remain - raw[i], i + 1)
            # back_trace 返回，代表remain <= 0，当前的temp已经无法进行下去了，移除最后一位，继续尝试下一个数
            temp.pop(len(temp) - 1)


# TODO:: 动态规划的解法


def calc(raw: list, target: int) -> list:
    res = []
    raw.sort()
    back_trace(res, [], raw, target, 0)
    return res


if __name__ == "__main__":
    print(calc([2, 3, 6, 7], 7))
    print(calc([10, 1, 2, 7, 6, 1, 5], 4))
