"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。


以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。


图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

输入: [2,1,5,6,2,3]
输出: 10
"""

# 暴力法 遍历所有可能的高度，找到每个高度可能的面积，算出最大值
# 时间复杂O(n^2) 报超时~
def max_area(nums:list) -> int:
    hight_set = set(nums)
    res = 0
    for hight in hight_set:
        count = 0
        for i in nums:
            if i >= hight:
                count += 1
            else:
                count = 0
            area = hight * count
            res = max(area, res)
    return res

def get_min(nums:list, start:int, end:int) -> int:
    min_index = start
    for i in range(start, end + 1):
        if nums[i] < nums[min_index]:
            min_index = i
    return min_index

"""
思路类似快排，将柱子分成两部分，最大的面积可能再左边部分，右边部分，或者跨过中间的柱子
中间的柱子如何选，只能选最小的那根柱子，由于中间柱子最小，所以其他的柱子一定都能算进面积中
这时最大值一定是(end - start + 1) * min
因为最坏情况下，求柱子的最小值为O(n)
leetcode 依然超时~
"""
def max_area2(nums:list, start:int, end:int) -> int:
    if start == end:
        return nums[start]
    if start > end:
        return -1
    min_index = get_min(nums, start, end)
    # print('min_index:', min_index)
    area1 = (end - start + 1) * nums[min_index]
    area2 = max_area2(nums, start, min_index - 1)
    area3 = max_area2(nums, min_index + 1, end)
    # print(area1, area2, area3)
    return max(area1, area2, area3)


"""
解法一是通过暴力法，根据矩形的高度分类，再计算各个高度矩形面积的最大值，最后得到整个的最大值
调整分类的方法，遍历所有的柱子，计算每个含有当前柱子的面积最大值，此时矩形高度一定为当前柱子的高度
宽度为左边的第一个比当前柱子短的距离加上右边第一个比当前柱子短柱子的距离
求左右的宽度，复杂度为O(n) 可通过动态规划的思想优化
记录每个柱子第一个比当前小的柱子的位置，时间复杂度为O(n)
"""
def max_area3(nums:list) -> int:
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
        


if __name__ == "__main__":
    nums = [2,1,5,6,2,3]
    print(max_area(nums))
    print(max_area2(nums, 0, len(nums) - 1))
    print(max_area3([1, 1]))