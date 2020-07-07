'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true

示例 3:

输入: "(]"
输出: false

示例 4:

输入: "([)]"
输出: false

示例 5:

输入: "{[]}"
输出: true

思路：
维护一个队列 和一个临时变量（最后一个左括号）
遍历字符串，如果是左括号塞入队列，否则判断是否和变量相等
相等则说明当前匹配正确，pop队列，并修改临时变量
'''

mapping={'}':'{', ']':'[', ')':'('}

def check(input:str)->bool:
    res = True

    if input == '':
        return res

    queue=[]
    last = ''
    for i in input:
        if i in ['[', '{', '(']:
            queue.append(i)
            last = i
        else:
            if last == mapping[i]:
                queue.pop()
                if len(queue) > 0:
                    last=queue[len(queue) - 1]
                else:
                    last=''
            else:
                res = False
                break

    return res

if __name__ == "__main__":
    input='([)]'
    print(check(input))