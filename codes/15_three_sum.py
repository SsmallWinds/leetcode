'''
题目描述
给定一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 *a，b，c ，*使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

题目解析
题目需要我们找出三个数且和为 0 ，那么除了三个数全是 0 的情况之外，肯定会有负数和正数，
所以一开始可以先选择一个数，然后再去找另外两个数，这样只要找到两个数且和为第一个选择的数的相反数就行了。也就是说需要枚举 a 和 b ，将 c 的存入 map 即可。

需要注意的是返回的结果中，不能有有重复的结果。这样的代码时间复杂度是 O(n^2)。
在这里可以先将原数组进行排序，然后再遍历排序后的数组，这样就可以使用双指针以线性时间复杂度来遍历所有满足题意的两个数组合。
'''

# 用 0 减去当前数得到差值， 再找差的两数之和即可
def calc(input:list)->list:
    res = []
    input.sort()
    for i in range(len(input) - 2):
        # 因为已经排过序了, 遇到和上一个值相同的值直接跳过即可
        if i > 0 and input[i] == input[i - 1]:
            continue
        # 定义双指针和目标值
        left = i + 1
        right = len(input) - 1
        target = 0 - input[i]
        while left < right:
            if input[left] + input[right] == target:
                res.append([input[i],input[left],input[right]])
                # 遇到相同的值直接跳过
                while left < right and input[left] == input[left + 1]:
                    left += 1
                while left < right and input[right] == input[right - 1]:
                    right -= 1
                # 由于已经经过排序，可能的解只能是往里缩
                left += 1
                right -= 1
            # 小于目标值，左边向右找
            elif input[left] + input[right] < target:
                left += 1
            # 大于目标值，右边向左找
            else:
                right -= 1
    return res

if __name__ == '__main__':
    input=[-4, -3, -2, -1, 1, 2, 2]
    print(calc(input))