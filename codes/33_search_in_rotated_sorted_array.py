"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

分析：
二分为左右两部分，一定有一部分是有序的，判断方法为子串左端是否小于右端
判断target是否在有序的部分，否则在另外的部分
"""


# 正常二分
def find(raw: list, start: int, end: int, target: int) -> int:
    if start <= end:
        mid = int(start + (end - start) / 2)
        if target < raw[mid]:
            return find(raw, start, mid - 1, target)
        elif target > raw[mid]:
            return find(raw, mid + 1, end, target)
        else:
            return mid
    else:
        return -1


def find2(raw: list, target: int) -> int:
    start = 0
    end = len(raw) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if raw[mid] == target:
            return mid
        # 如果左半段有序
        if raw[start] < raw[mid]:
            # 在左半部分
            if raw[start] <= target < raw[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # 在右半部分
            if raw[mid] < target <= raw[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def search(raw: list, target: int) -> int:
    return find2(raw, target)


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 1))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
