"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""

def add_bin(a:str, b:str) -> str:
    lena = len(a)
    lenb = len(b)
    index = 0
    carry = 0
    res = ''
    while index < lena or index < lenb:
        vala = 0
        valb = 0
        if index < lena:
            vala = int(a[lena - index - 1])
        if index < lenb:
            valb = int(b[lenb - index - 1])

        sum = vala + valb + carry
        res = str(int(sum % 2)) + res
        carry = int(sum / 2)
        index += 1
    if carry == 1:
        res = '1' + res
    return res

if __name__ == "__main__":
    print(add_bin('1111', '1111'))