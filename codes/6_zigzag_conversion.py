'''
题目描述
给定一个字符串，和一个整数n，将它排列成一个n行的蛇形返回。

示例
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
给定字符串和蛇形排列占据的行数，要求返回重新排列后的串
'''

def calc(input:str, num_rows:int)->str:
    rows=['' for _ in range(num_rows)]
    if num_rows == 1:
        return input
    cur_row=0
    forward=True # 从上往下

    for c in input:
        rows[cur_row] += c
        if forward:
            cur_row += 1
        else:
            cur_row -= 1
        # 到底了,掉头
        if cur_row == num_rows - 1 and forward:
            forward = False
        # 到顶了,掉头
        if cur_row == 0 and not forward:
            forward = True
    print(rows)
    return ''.join(rows)

if __name__ == "__main__":
    input='PAYPALISHIRING'
    num_rows=4
    print(calc(input, num_rows))