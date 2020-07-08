'''
题目描述
给定数字n，要求使用n对()括号生成所有合法的组合情况。

示例

3

[
"((()))",
"(()())",
"(())()",
"()(())", 
"()()()"
]

'''

#1 暴力法，遍历所有可能的组合，返回合法的组合
def check(input:str)->bool:
    res = True

    if input == '':
        return res

    balance = 0
    for i in input:
        if i == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                res = False
                return res

    res = balance == 0
    return res

def gen(lenght:int, prefix:str, res:list)->None:
    if lenght <= 0:
        res.append(prefix)
        return
    
    gen(lenght - 1, prefix + ')', res)
    gen(lenght - 1, prefix + '(', res)

def calc1(input:int)->list:
    temp = []
    res = []
    gen(input*2, '', temp)
    for item in temp:
        if check(item):
            res.append(item)
    return res

# 2.直接根据规律生成
# 生成时，如果左括号 > n 结果一定非法
# 如果右括号 > 左括号一定非法
# 生成时，直接过滤掉非法字符串,剩下的即为结果

def gen2(n:int, lenght:int, prefix:str, res:list, left:int, right:int)->None:
    if lenght <= 0:
        res.append(prefix)
        return
    if right + 1 <= left:
        gen2(n, lenght - 1, prefix + ')', res, left, right + 1)
    if left < n:
        gen2(n, lenght - 1, prefix + '(', res, left + 1, right)

def calc2(input:int)->list:
    res = []
    gen2(input, input*2, '', res, 0, 0)
    return res

# 解法3,TODO::
# https://leetcode.wang/leetCode-22-Generate-Parentheses.html

if __name__ == "__main__":
    input = 4
    print(calc1(input))
    print(calc2(input))