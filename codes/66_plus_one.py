"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

思路：
顺着题意处理即可，注意进位的处理
"""

def plus_one(num:list) -> list:
    for i in range(len(num) - 1, -1, -1):
        if num[i] < 9:
            num[i] += 1
            break
        else:
            num[i] = 0

    if num[0] == 0:
        return [1] + num
    return num

if __name__ == "__main__":
    print(plus_one([9,9,9,9]))