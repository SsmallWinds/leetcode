"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

思路：
二分找到后，左右拓展, 最坏情况的时间复杂度是 O(n)
优化
找到值后，不返回，继续二分分别找到左右边界，时间复杂度为 O(2n) -> O(n)
"""


def find(raw: list, target: int) -> tuple:
    start = 0
    end = len(raw) - 1
    res = -1
    while start <= end:
        mid = int((end + start) / 2)
        if target < raw[mid]:
            end = mid - 1
        elif target > raw[mid]:
            start = mid + 1
        else:
            res = mid
            break
    if res == -1:
        return -1, -1

    left, right = res, res
    while left >= 0 and raw[left] == target:
        left -= 1
    while right <= len(raw) and raw[right] == target:
        right += 1
    return left + 1, right - 1


def find2(raw: list, target: int) -> tuple:
    start = 0
    end = len(raw) - 1
    res_l = -1
    while start <= end:
        mid = int((end + start) / 2)
        if target < raw[mid]:
            end = mid - 1
        elif target > raw[mid]:
            start = mid + 1
        else:
            # 找到相等的后，不是跳出循环，而是继续向左查找
            end = mid - 1

    # 没有找到target直接返回 -1
    if start >= len(raw) or raw[start] != target:
        return -1, -1
    else:
        res_l = start

    # 继续找右边界
    start = 0
    end = len(raw) - 1
    while start <= end:
        mid = int((end + start) / 2)
        if target < raw[mid]:
            end = mid - 1
        elif target > raw[mid]:
            start = mid + 1
        else:
            # 找到相等的后，不是跳出循环，而是继续向右查找
            start = mid + 1
    return res_l, end


if __name__ == "__main__":
    print(find2([5, 7, 7, 7, 8, 8, 10], 7))
