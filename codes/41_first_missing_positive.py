"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
 

提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。

思路：
先不考虑空间复杂度O(1)的限制
利用一个n 长度的数组
遍历输入，当raw[i] 为正数且<=n时，将temp[raw[i] - 1]置为 raw[i]
[1, 2, 0] ->[1, 2, -1]
[1, -1, -1] ->[1, -1, -1]
[7, 8, 9] ->[-1, -1, -1]
很容易推断出结果，第一个temp[i - 1] != i 的i值，即为结果
当全部都不满足结果时，说明1-n 全部都存在，则结果为 n+1

需要空间复杂度为常数时，可借用原数组保存
遍历输入，当raw[i]为正数且 n<=n时，且当i != raw[i] - 1时(在范围内且第i个位置不是i)
将位置i 和 位置raw[i] 交换直到符合条件
遍历完成后，结果应该是和temp类似，判断第一个raw[i - 1] != i 的位置为结果
全部满足则结果是n+1

"""


def first_missing(raw: list) -> int:
    temp = [-1 for _ in range(len(raw))]
    for i in range(len(raw)):
        if raw[i] <= 0 or raw[i] > len(raw):
            continue
        else:
            temp[raw[i] - 1] = raw[i]

    for i in range(len(temp)):
        if temp[i] != i + 1:
            return i + 1
    return len(temp) + 1


def swap(raw: list, a: int, b: int):
    temp = raw[a]
    raw[a] = raw[b]
    raw[b] = temp


def first_missing2(raw: list) -> int:
    for i in range(len(raw)):
        while 0 < raw[i] <= len(raw) and i != raw[i] - 1:
            swap(raw, i, raw[i] - 1)

    for i in range(len(raw)):
        if raw[i] != i + 1:
            return i + 1
    return len(raw) + 1


if __name__ == "__main__":
    print(first_missing([1, 2, 0]))
    print(first_missing([1, -1, -1]))
    print(first_missing([7, 8, 9]))
    print(first_missing([3, 4, -4, 1]))
    print(first_missing([1, 2, 3, 4]))

    print('-----------')
    print(first_missing2([1, 2, 0]))
    print(first_missing2([1, -1, -1]))
    print(first_missing2([7, 8, 9]))
    print(first_missing2([3, 4, -4, 1]))
    print(first_missing2([1, 2, 3, 4]))
