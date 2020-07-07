'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
mapping=['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def mul(s1:str,s2:str)->list:
    res = []
    for a in s1:
        for b in s2:
            res.append(a + b)
    return res

# 数组相乘 res = a * b * c
def calc(input:str)->list:
    res = [i for i in mapping[int(input[0]) - 2]]
    for num in input[1:]:
        res = mul(res, mapping[int(num) - 2])
    return res

# 递归的方法；
# 递归过程：
# [] -> ['a', 'b', 'c'] -> ['ad', 'ae', 'af'....]
# prefix 记录每一层的结果，递归的终止条件是prefix的长度 == lend(digits) 即输入数字的数量，最终结果的总数是 len('abc') * len('def') * ....
def combi(prefix:str, digits:str, offset:int, res:list)->None:
    if offset == len(digits):
        res.append(prefix)
        return

    for l in mapping[int(digits[offset]) - 2]:
        combi(prefix+l, digits, offset + 1, res)

def calc2(input:str)->list:
    res = []
    combi('', input, 0, res)
    return res

if __name__ == '__main__':
    input='23'
    print(calc(input))
    print(calc2(input))