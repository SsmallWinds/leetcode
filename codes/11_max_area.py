'''
题目描述：

给你n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i,ai)。在坐标内画n条垂直线，
垂直线i的两个端点分别为(i,ai)和(i,0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且n的值至少为2。
示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
很容易的可以得到---->容器可以容纳水的容量=两条垂直线中最短的那条*两条线之间的距离
现在的情况是，有很多条线，让你计算两两之间能装的最多的水，
其实暴力法之间就能解决这个问题，但是它的时间复杂度也达到了O(n^2)

分析：
容量 = (j - i) * min(ai, aj)
'''

# 直接暴力法，遍历所有的i和j,得到容量最大的即为结果,时间复杂度为 O(n^2)
def calc(input:list)->int:
    res = 0
    for i in range(len(input)):
        for j in range(i + 1,len(input)):
            res = max((j - i) * min(input[i], input[j]), res)
    return res

# 维护左右两个指针， 尝试向里缩， 
# 当左边对应的高度高时缩右边，反之缩左边， 取过程中计算得到的最大值，时间复杂度为O(n)
def calc2(input:list)->int:
    left,right = 0, len(input) - 1
    res = 0
    while left < right:
        if input[left] >= input[right]:
            res = max(res, (right - left) * input[right])
            right -= 1
        else:
            res = max(res, (right - left) * input[left])
            left += 1
    return res

if __name__ == "__main__":
    input=[1,8,6,2,5,4,8,3,7]
    print(calc(input))
    print(calc2(input))