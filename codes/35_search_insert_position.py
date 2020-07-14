"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

思路：
二分都是会缩到一个点上

小于所有，则缩到 0
大于所有，则缩到 n
找到了，则缩到找到的位置
"""


def search(raw: list, target: int) -> int:
    start = 0
    end = len(raw) - 1
    res = -1
    while start <= end:
        mid = int((end + start) / 2)
        # 大于往右找
        if target > raw[mid]:
            start = mid + 1
        # 小于等于都是往左找
        else:
            end = mid - 1
    return start


if __name__ == '__main__':
    print(search([1, 3, 4, 6], 7))
