"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
https://leetcode-cn.com/problems/trapping-rain-water

思路：
可以按列一个一个求
min = min(left_max, right_max)
如果 cur >= min 当前列的容量为0
否则 当前列的容量是 min - cur
时间复杂度是O(n^2)

求left_max 和 right_max的时候可以用动态规划
将时间复杂度优化为O(n)

"""


# 分别求每列的容量，时间复杂度是O(n^2)
def calc(raw: list) -> int:
    res = 0
    for i in range(len(raw)):
        left_max = -1
        right_max = -1
        left = [raw[j] for j in range(i)]
        if len(left) > 0:
            left_max = max(left)
        right = [raw[k] for k in range(i + 1, len(raw))]
        if len(right) > 0:
            right_max = max(right)
        if left_max < 0 or right_max < 0:
            continue
        min_val = min(left_max, right_max)
        if min_val > raw[i]:
            res += (min_val - raw[i])

    return res


# 最大值和最小值先生成好, 时间复杂度为 O(3n) => O(n)
def calc2(raw: list) -> int:
    left_max = [0 for _ in raw]
    right_max = [0 for _ in raw]
    res = 0
    for i in range(1, len(raw) - 1):
        left_max[i] = max(left_max[i - 1], raw[i - 1])
    for i in range(len(raw) - 2, 1 - 1, -1):
        right_max[i] = max(right_max[i + 1], raw[i + 1])
    for i in range(1, len(raw) - 1):
        min_val = min(left_max[i], right_max[i])
        if min_val > raw[i]:
            res += (min_val - raw[i])

    return res


# TODO 优化空间复杂度 https://leetcode.wang/leetCode-42-Trapping-Rain-Water.html


if __name__ == "__main__":
    print(calc2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
