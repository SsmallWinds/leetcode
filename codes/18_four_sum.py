'''
题目描述
给定一个包含 n 个整数的数组 nums，和target
判断 nums 中是否存在四个元素 *a，b，c ，d*使得 a + b + c + d = target ？找出所有满足条件且不重复的四元组。

题目解析
题目需要我们找出四个数且和为 target
方法和三数之和类似
'''

# 用 target 减去当前数(i, j)得到差值， 再找差的两数之和即可,时间复杂度是O(n^3)
def calc(input:list, target:int)->list:
    res = []
    input.sort()
    for i in range(len(input) - 3):
        if i > 0 and input[i] == input[i - 1]:
            continue
        for j in range(i + 1, len(input) - 2):
            if j > i + 1 and input[j] == input[j - 1]:
                continue
            sub = target - input[i] - input[j]
            # 剩下的是找 k, l 满足 sub = input[k] + input[l]
            left = j + 1
            right = len(input) - 1
            while left < right:
                sub2 = input[left] + input[right]
                if sub2 == sub:
                    res.append([input[i], input[j], input[left], input[right]])
                    while left < right and input[left] == input[left + 1]:
                        left += 1
                    while left < right and input[right] == input[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sub2 > sub:
                    right -= 1
                else:
                    left += 1

    return res

if __name__ == '__main__':
    input=[1,2,3,-1,-2,-3]
    print(calc(input, 0))