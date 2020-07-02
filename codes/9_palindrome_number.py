'''
题目描述
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''

# 最简单的方法，转成字符串，判断反转前后是否相等
def calc(input:int)->bool:
    input=str(input)
    return input == input[::-1]

# 计算方法
def calc2(input:int)->bool:
    res = True
    div = 1
    while input / div >= 10:
        div *= 10

    while input > 0:
        left = int(input / div)
        right = input % 10
        #print(left)
        #print(right)
        if left != right:
            res = False
            break
        else:
            div = int(div / 100)
            input = int((input % div) / 10)

    return res

if __name__ == "__main__":
    input = 1221
    print(calc(input))
    print(calc2(input))