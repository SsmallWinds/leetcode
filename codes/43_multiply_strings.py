"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

思路：
先按位相乘，再将各个位的结果用大数相加
"""


def add(a: str, b: str) -> str:
    if len(a) > len(b):
        b = ''.join(['0' for _ in range(len(a) - len(b))]) + b
    if len(b) > len(a):
        a = ''.join(['0' for _ in range(len(b) - len(a))]) + a
    index = len(a) - 1
    carry = 0
    res = ''
    while index >= 0:
        a_val = 0
        b_val = 0
        if index < len(a):
            a_val = int(a[index])
        if index < len(b):
            b_val = int(b[index])
        temp = a_val + b_val + carry
        carry = int(temp / 10)
        res += str(temp % 10)
        index -= 1
    if carry > 0:
        res += str(carry)
    return res[::-1]


def multiply_single(s: str, b: int) -> str:
    res = ''
    carry = 0
    for i in s[::-1]:
        temp = int(int(i) * b + carry)
        res += str((temp % 10))
        carry = int(temp / 10)
    if carry > 0:
        res += str(carry)
    return res[::-1]


def multiply(a: str, b: str) -> str:
    res = '0'
    bit = 0
    for i in a[::-1]:
        temp = multiply_single(b, int(i))
        for j in range(bit):
            temp += '0'
        bit += 1
        res = add(res, temp)

    return res


if __name__ == "__main__":
    print(add('1234', '12'))
    print(multiply_single('123456789123456789', 1))
    print(multiply('123456789123456789', '123456789123456789'))
    print(multiply('0', '0'))
