'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

# 获取最短的字符串长度，从0开始比较，直到不同的位置
def calc(input:list)->str:
    res = ''
    length=len(min(input, key=lambda k: len(k)))

    for i in range(length):
        val=input[0][i]
        same=True
        for j in range(1, len(input)):
            same = val == input[j][i] and same
        if same:
            res += val
        else:
            break

    return res

if __name__ == '__main__':
    input=["flower","flow","floight"]
    print(calc(input))
