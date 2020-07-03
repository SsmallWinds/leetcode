'''
题目描述:
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例:
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
思路:
一句话解释:固定一个值,找另外两个值(双指针).

数组是排好序的，先确定一个数,另外两个数用左右指针表示，在运动过程中,记录与target绝对值差值最小的.
'''

# 和15题思路类似 用 target 减去当前数得到差值， 再在剩下的值中找与target差绝对值最小的
def calc(input:list, target:int)->list:
    import sys
    res = None
    sub = sys.maxsize
    input.sort()
    for i in range(len(input) - 2):
        # 定义双指针和目标值
        left = i + 1
        right = len(input) - 1
        while left < right:
            sum = input[i] + input[left] + input[right]
            # 找到较小的差值记录下来
            if abs(sum - target) < sub:
                res = [input[i],input[left],input[right]]
                sub = abs(sum - target)
            # 小于目标值，左边向右找
            if sum < target:
                left += 1
            # 大于目标值，右边向左找
            else:
                right -= 1
    return res, sub

if __name__ == '__main__':
    input=[-1, 2, 1,-4]
    print(calc(input, 1))