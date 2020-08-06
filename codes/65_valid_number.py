"""
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

思路：
有限状态机

状态:
见图 65_1.jpg
难点是画出状态转换图，时间代码就是正常有限状态机的套路即可
"""
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mark = ['+', '-']
power = ['e']
point = ['.']

def check(s: str) -> bool:
    state = 0
    for i in s:
        if i in mark:
            if state == 0:
                state = 1
            elif state == 4:
                state = 6
            else:
                return False
        elif i in num:
            if state == 0 or state == 1 or state == 2:
                state = 2
            elif state == 3:
                state = 3
            elif state == 7 or state == 8:
                state = 8
            elif state == 4 or state == 5 or state == 6:
                state = 5
            else:
                return False
        elif i in power:
            if state == 8 or state == 2 or state == 3:
                state = 4
            else:
                return False
        elif i in point:
            if state == 0 or state == 1:
                state = 7
            elif state == 2:
                state = 3
            else:
                return False
        else:
            return False
    
    return state in [2, 3, 5, 8]


if __name__ == "__main__":
    print(check("12345"))