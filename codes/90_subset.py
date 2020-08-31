"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

1.回溯法，和78题基本一致，为除重，需要先将nums排序
循环中判断当前值和上个值是否相同，相同则跳过
2.位运算，思路和78题一致，也是利用1含0不含的方式判断是否要加入
去重的思路是，当前数字和上一个数字相同时，需要判断是否需要加入，
选择上一个也是1的加入
例如 222。连续3个2,选两个会有110 101 011 三种方式
选择有连续两个1的方式，即判断上一个为0时就可以跳过了
很巧妙的思路，将所有的可能列出，找规律

"""


def do_sub_set(nums: list, res: list, temp: list, index: int) -> list:
    from copy import copy
    res.append(copy(temp))

    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        temp.append(nums[i])
        do_sub_set(nums, res, temp, i + 1)
        temp.pop()


def sub_set(nums: list) -> list:
    res = []
    nums.sort()
    do_sub_set(nums, res, [], 0)
    return res


def sub_set2(nums: list) -> list:
    res = []
    nums.sort()
    count = 1 << len(nums)
    for i in range(count):
        temp = []
        is_valid = True
        for j in range(len(nums)):
            if (i >> j) & 1:
                if j > 0 and nums[j] == nums[j - 1] and (i >> j - 1) & 1 == 0:
                    is_valid = False
                    break
                else:
                    temp.append(nums[j])
        if is_valid:
            res.append(temp)
    return res


if __name__ == "__main__":
    nums = [1, 2, 2, 2]
    print(sub_set(nums))
    print(sub_set2(nums))
