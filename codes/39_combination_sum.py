"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""


# 回溯法
# 回溯法的套路是一个大的循环，先add，然后递归向前遍历，再remove， 继续循环
def back_trace(res: list, temp: list, raw: list, remain: int, start: int) -> None:
    import copy
    if remain < 0:
        return
    elif remain == 0:
        res.append(copy.copy(temp))
        return
    else:
        for i in range(start, len(raw)):
            temp.append(raw[i])
            # 可重复使用，所以传入的i不变，若题目改为不能重复使用，则传入i + 1 即可
            back_trace(res, temp, raw, remain - raw[i], i)
            # back_trace 返回，代表remain <= 0，当前的temp已经无法进行下去了，移除最后一位，继续尝试下一个数
            temp.pop(len(temp) - 1)


# TODO:: 动态规划的解法


def calc(raw: list, target: int) -> list:
    res = []
    back_trace(res, [], raw, target, 0)
    return res


if __name__ == "__main__":
    print(calc([2, 3, 6, 7], 7))
    print(calc([2, 3, 5, 7], 8))
