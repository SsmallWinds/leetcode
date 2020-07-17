"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
"""


# 直接累乘或累除 时间复杂度是 O(n)
def my_pow(x: float, n: int) -> float:
    res = 1
    if n == 0:
        res = 1
    elif n > 0:
        while n > 0:
            res *= x
            n -= 1
    else:
        n = -n
        while n > 0:
            res /= x
            n -= 1

    return res


def my_pow2_helper(x: float, n: int) -> float:
    if n == 0:
        return 1

    temp = my_pow2_helper(x, int(n / 2))
    # 偶数
    if n % 2 == 0:
        return temp * temp
    else:
        return temp * temp * x


# 利用a^b = a^(b/2) * a^(b/2) 注意区分奇数和偶数的情况
# 事件复杂度为 O(Log n)
def my_pow2(x: float, n: int) -> float:
    if n < 0:
        n = -n
        return 1 / my_pow2_helper(x, n)
    else:
        return my_pow2_helper(x, n)


if __name__ == "__main__":
    print(my_pow(2, -10))
    print(my_pow2(2, -10))
