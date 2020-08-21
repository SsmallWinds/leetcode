"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

思路：
回溯法
1.基于 题77， 将所有长度的子集都遍历一遍
2.优化，不需要每次重复，回溯过程中的解都记录下来即可

特殊解法：
位操作
每个数字都只有在或者不在子集中两种可能
所以对于 [1,2,3] , 解为 000 - 111 ，其中 0表示不存在 1表示存在 
例如 000 -> [] 010 -> [2] 111->[1,2,3]
数量为2^n
"""

from copy import copy

def pick(temp:list, res:list, start:int, n:int, nums:list) -> None:
    if len(temp) == n:
        res.append(copy(temp))
        return
    
    for i in range(start, len(nums)):
        temp.append(nums[i])
        pick(temp, res, i + 1, n, nums)
        temp.pop()

def subset(nums:list) -> list:
    res = []
    for i in range(len(nums) + 1):
        pick([], res, 0, i, nums)
    return res

def do_subset(temp:list, res:list, start:int, nums:list) -> None:
    res.append(copy(temp))
    for i in range(start, len(nums)):
        temp.append(nums[i])
        do_subset(temp, res, i + 1, nums)
        temp.pop()

def subset2(nums:list) -> list:
    res = []
    do_subset([], res, 0, nums)
    return res

def subset3(nums:list) -> list:
    res_len = 1 << len(nums)
    res = []
    for i in range(res_len):
        temp = []
        for j in range(len(nums)):
            if (i >> j) & 1:
                temp.append(nums[j])
        res.append(temp)
    return res


if __name__ == "__main__":
    print(subset2([1,2,3]))
    print(subset3([1,2,3]))