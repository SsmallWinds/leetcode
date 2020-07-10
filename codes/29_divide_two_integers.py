'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，
其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

思路：
先判断符号，将两个数都转换为正数
用除数循环减被除数即可

优化：
每次减n 可优化成 减n, 2n ...,剩下的再递归处理

'''

def divide(dividend:int, divisor:int)->int:
    positive = not (dividend < 0) ^ (divisor < 0)
    if dividend < 0:
        dividend = 0 - dividend
    if divisor < 0:
        divisor = 0 - divisor
    
    res = 0
    while dividend > divisor:
        dividend -= divisor
        res += 1
    
    return res if positive else 0 - res

def divide2(dividend:int, divisor:int)->int:
    positive = not (dividend < 0) ^ (divisor < 0)
    if dividend < 0:
        dividend = 0 - dividend
    if divisor < 0:
        divisor = 0 - divisor

    if dividend < divisor:
        return 0
    
    res = 0
    div = divisor
    level = 1
    while dividend >= div:
        dividend -= div
        res += level
        div += div
        level += level
    
    print('res:%d'%res)
    print('dividend:%d'%dividend)
    return (res if positive else 0 - res) + divide2(dividend, divisor)

if __name__ == "__main__":
    print(divide(-7, 3))
    print(divide2(5234, 3))