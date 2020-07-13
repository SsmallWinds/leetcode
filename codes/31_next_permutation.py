"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

思路：
组合的大小左边的数权重大于右边的数
所以找下一个更大的排列
需要从右往左找到第一个降序的值 eg. 1584765431 找到 4，
这个位置代表 1584 开头能表达的最大的数，想找下一个更大的数，则需要找能变大的权重最小的位置4
想变大就要找一个比4大的数与其交换，左边不可能（左边权重大），故可在右边找一个最接近的值
再在4后面的降序序列中，找到最接近4的值，5
交换4和5 得到158576431 4->5后，右边现在是1585开头的能表达的最大的值
所以需要倒序，变成 158513467即为结果
"""


def swap(sz: list, a: int, b: int) -> None:
    temp = sz[a]
    sz[a] = sz[b]
    sz[b] = temp


def reverse(sz: list, a: int, b: int) -> None:
    while a < b:
        swap(sz, a, b)
        a += 1
        b -= 1


def next_permutation(raw: list) -> list:
    import sys
    temp = -1
    for i in range(len(raw) - 1, 0, -1):
        if raw[i - 1] < raw[i]:
            temp = i - 1
            break

    if temp == -1:
        # 找不到,直接倒转
        reverse(raw, 0, len(raw) - 1)
        return raw

    # 找到temp右边最接近的值
    minimal = sys.maxsize
    temp2 = -1
    for i in range(temp + 1, len(raw)):
        diff = abs(raw[i] - raw[temp])
        if diff < minimal:
            minimal = diff
            temp2 = i
    swap(raw, temp, temp2)
    reverse(raw, temp + 1, len(raw) - 1)
    return raw


if __name__ == "__main__":
    print(next_permutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))
    print(next_permutation([1, 2, 3, 4]))
    print(next_permutation([4, 3, 2, 1]))
