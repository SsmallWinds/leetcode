'''
题目描述
给定一个字符串，要求这个字符串当中最长的回文串。

示例
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Input: "cbbd"
Output: "bb"
'''

# 遍历所有index可能的奇数回文和偶数回文，时间复杂度为 O(n^2)
def calc(input:str)->str:
    begin=0
    res = 0
    for index in range(0,len(input)):
        # 判断奇数子串
        center = index
        i = 0
        while center - i >= 0 and center + i <= len(input) - 1:
            if input[center - i] == input[center + i]:
                i += 1
            else:
                break
        length = 1 + (i - 1) * 2
        if length > res:
            res = length
            begin = index - i + 1
        
        # 判读偶数子串
        left=index-1
        right=index
        while left >= 0 and right <= len(input) - 1:
            if input[left] == input[right]:
                left-=1
                right+=1
            else:
                break
        length=right - left - 1
        if length > res:
            res = length
            begin = left + 1
    return input[begin:begin + res]

# Manacher 方法
def calc2(input:str)->str:
    # 用'#'符号填充, 将奇数和偶数个的input统一为奇数,前后添加字符防止越界
    input='$#' + '#'.join(list(input)) + '#&'
    # p为每个位置构成的合法回文串半径
    p=[0 for _ in range(len(input) + 1)]
    # mr为当前位置能够构成回文串向右最远的位置
    # _id是这个位置对应的回文串中心
    mr, _id = 0, 0
    for i in range(1,len(input) -1):
        # i_mirror 是 i 对于 _id 的对称点，
        # ml<- i_mirror <- _id ->i -> mr 是当前位置最长的已确认的回文子串，由于回文的对称性，在 _id -> mr 范围内的，且右边界不超过 mr的部分满足p[i_mirror] == p[i]
        # 1.对称点的值p[i_mirror]只能保证到mr的时候一定是回文，超出的mr部分需要继续用以mr-i为起点使用中心拓展法
        # 2.p[i_mirror] 对应的回文遇到左边界时，p[i]可能可以继续拓展，所以可以直接基于p[i]使用中心拓展法
        # 3.当mr <= i 时相当于是还没有对称点的值，直接以从1 开始使用中心拓展法即可
        i_mirror = 2 * _id - i
        p[i] = 1 if mr <= i else min(p[i_mirror], mr - i)
        while input[i - p[i]] == input[i + p[i]]:
            p[i] += 1

        # 调整 mr 和 _id的位置
        if i + p[i] > mr:
            mr, _id = i + p[i], i
    _id = p.index(max(p))
    res = input[_id - p[_id] + 1: _id + p[_id]]
    return  ''.join(filter(lambda x: x != '#', list(res)))

if __name__ == "__main__":
    input='bsdfsaasfddb'
    print(calc(input))
    print(calc2(input))