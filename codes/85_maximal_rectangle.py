"""
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""
import sys


# 暴力法，遍历每一个点，计算以每个点开头的矩形的面积最大值
# 计算方式为，以高度为1向下扩充，直到遇到 ‘0’, 宽度为过程中的最小值
def max_rect(nums: list) -> int:
    def get_width(nums: list, row: int, col: int) -> int:
        res = 0
        for i in range(col, len(nums[0])):
            if nums[row][i] != '1':
                break
            res += 1
        return res

    res = 0
    width = len(nums[0])
    height = len(nums)
    for i in range(height):
        for j in range(width):
            cur_width = sys.maxsize
            cur_height = 1
            for k in range(i, height):
                if nums[k][j] == '1':
                    cur_width = min(cur_width, get_width(nums, k, j))
                    area = cur_height * cur_width
                    cur_height += 1
                    res = max(res, area)
                else:
                    break

    return res


def max_area3(nums: list) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    left_min = [0 for _ in nums]
    left_min[0] = -1
    for i in range(1, len(nums)):
        cur = i - 1
        while cur >= 0 and nums[i] <= nums[cur]:
            cur = left_min[cur]
        # print(i, cur)
        left_min[i] = cur

    # print(left_min)
    right_max = [0 for _ in nums]
    right_max[-1] = len(nums)
    for i in range(len(nums) - 1, -1, -1):
        cur = i + 1
        while cur < len(nums) and nums[i] <= nums[cur]:
            cur = right_max[cur]
        right_max[i] = cur

    # print(right_max)
    res = 0
    for i in range(len(nums)):
        left = left_min[i]
        right = right_max[i]
        res = max((right - left - 1) * nums[i], res)
    return res


"""
参考84题，84题是计算矩形的最大值
本题可以看成每层都可以用'1'的高度当成一个柱状图
每层最大矩形的时间复杂度是O(n)
遍历m层，总的时间复杂度是O(nm)
"""
def max_rect2(nums: list) -> int:
    heights = [0 for _ in nums[0]]
    width = len(nums[0])
    res = 0
    for row in nums:
        for i in range(width):
            if row[i] == '1':
                heights[i] += 1
            else:
                heights[i] = 0
            area = max_area3(heights)
            res = max(res, area)
    return res


"""
依旧是参考84题，优化了找left_min 和 right_max的过程
直接调用84题的方法，需要每次重新构建left_min 和 right_max的数组
在逐层构建left_min 和 right_max 的过程中，每一行的值可基于上一行获得
当前行为'1'的部分左边的第一个较小值是上一次出现0的位置和上一行值的较大值，即更靠近当前柱子的位置
同理右边部分的第一个较小值是从右往左遍历，上一次出现0的位置和上一行该值的较小值
通过left_min 和 right_max 计算面积
"""
def max_rect3(nums: list) -> int:
    width = len(nums[0])
    left_min = [-1 for _ in nums[0]]
    right_max = [width for _ in nums[0]]
    heights = [0 for _ in nums[0]]
    res = 0

    for row in nums:
        for i in range(width):
            if row[i] == '1':
                heights[i] += 1
            else:
                heights[i] = 0

        last_zero = -1
        for i in range(width):
            if row[i] == '1':
                left_min[i] = max(left_min[i], last_zero)
            else:
                left_min[i] = -1
                last_zero = i

        last_zero = width
        for i in range(width - 1, -1, -1):
            if row[i] == '1':
                right_max[i] = min(right_max[i], last_zero)
            else:
                right_max[i] = width
                last_zero = i

        for i in range(width):
            area = (right_max[i] - left_min[i] - 1) * heights[i]
            res = max(res, area)
    return res


if __name__ == "__main__":
    nums = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    print(max_rect(nums))
    print(max_rect2(nums))
    print(max_rect3(nums))
